
from platform import libc_ver
import scipy.fftpack as sf
from scipy.io import wavfile
from scipy.signal import find_peaks
import numpy as np
import sys
from matplotlib import pyplot as plt
import os
import pyaudio
import math
import wave
import sounddevice as sd
import soundfile as sf
import queue

q = queue.Queue()

sys.path.append("..")
sys.path.append("../plugins")
sys.path.append("../pages")
sys.path.append("../system")

## IMPORT PLUGINS AND MODULES
import g, gui, styles
import time
import _thread
from fpdf import FPDF

if g.os == "win":
    import winsound

audio = pyaudio.PyAudio()
CHUNK_TIME = 0.05
PEAK_PROMINENCE = 0.25
SAMPLING_TIME = 0.15



def preshow(arg):
    if "quickpreview" in arg.__dict__:
        ## Quick View Functions Here
    
        return True

    arg.handles.pg_project.records.obj.config(selectmode='multiple')
    
    arg.handles.pg_project.labelTitle.obj.config(text="Project: " + arg.currentProject)
    arg.records = sorted([file for file in os.listdir('database/' + arg.currentProject) if file.endswith('.txt')])

    # Populate Data
    gui.listbox_data(arg, arg.handles.pg_project.records, arg.records)

    arg.recordState = False

    return True

def postshow(arg):
    return True

def back(arg):
    gui.showPage(arg, 'pg_main')


def viewRecord(arg):
    selection = arg.handles.pg_project.records.obj.curselection()

    if len(selection) == 0:
        gui.msgbox(arg, "No record selected.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return
    
    if len(selection) > 1:
        gui.msgbox(arg, "Choose only one record.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return
    
    idx = selection[0]

    arg.currentRecord = arg.records[idx]

    gui.showPage(arg, 'pg_record')


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def newRecord(arg):

    if arg.recordState == False:
        arg.handles.pg_project.btnRecord.obj.config(text="Stop Recording")  
        arg.trigRecording = True
        arg.recordState = True
        _thread.start_new_thread(threadRecordAudio, (arg,))
        
    else:
        arg.handles.pg_project.btnRecord.obj.config(text="Transcribing...")
        arg.trigRecording = False
        gui.msgbox(arg, "Press ok to begin transcription. Please wait for results.", "ok", "info")
        
        while arg.recordState:
            time.sleep(1)
            continue

        # Read File
        Fs, y = wavfile.read('currentRecording.wav')

        print('Signal Length:', len(y))
        print('Sampling Rate:', Fs)
        # print(Fs)
        # sd.play(y, Fs)

        if len(y.shape) > 1:
            y = y[:,0]
        
        # Trim First 0.1 Sec
        y = y[int(round(0.1*Fs)):]

        # Onset Detection
        # Flip Negatives to Positives
        yAbs = np.abs(y)

        # Create Array Placeholder for Max Amplitudes in given Chunks
        yMaxAmplitudesByChunks = np.array([0] * int(math.ceil(len(yAbs) /  (CHUNK_TIME * Fs))))

        # Get Max Values within Chunk
        for ctr in range(0,len(yMaxAmplitudesByChunks)):
            yMaxAmplitudesByChunks[ctr] = max(yAbs[int(round(ctr*(CHUNK_TIME * Fs))):int(round((ctr+1)*(CHUNK_TIME * Fs)))])

        peakProminence = PEAK_PROMINENCE * max(yMaxAmplitudesByChunks)
        # Find Peaks in Chunks
        yPeaks = find_peaks(yMaxAmplitudesByChunks, prominence=peakProminence)[0].astype(int)

        # plt.plot(np.arange(len(yMaxAmplitudesByChunks)), yMaxAmplitudesByChunks)
        # plt.plot(yPeaks, yMaxAmplitudesByChunks[yPeaks])
        # plt.show()

        # Get Frame Splits
        frameSplits = [0] * len(yPeaks)
        for ctr in range(0, len(frameSplits)):
            frameSplits[ctr] = int(yPeaks[ctr] * (CHUNK_TIME * Fs))

        # Get Dominant Notes Within Splits
        finalNotes = [()] * (len(frameSplits))

        previous1Response = None
        previous2Response = None

        for ctr in range(0, len(frameSplits)):

            yCurrent = y[frameSplits[ctr]:frameSplits[ctr]+int(round(SAMPLING_TIME * Fs))]
            try:
                yFreq, previous1Response, previous2Response = getFrequency(yCurrent, Fs, previous1Response, previous2Response)
            except BaseException as e:
                break

            # if g.os=="win":
            #     winsound.Beep(int(round(yFreq)), duration=400)
            
            if yFreq > 0:
                finalNotes[ctr] = frequency_to_note(yFreq)
        
        asciiTab = notesToAsciiTab(finalNotes)
        for line in asciiTab:
            print(line)

        # Get File Number
        ctr = 0
        while True:
            if os.path.exists('database/' + arg.currentProject + '/' + 'ascii' + '%03d' % (ctr) + '.txt'):
                ctr += 1
            else:
                break
        
        with open('database/' + arg.currentProject + '/' + 'ascii' + '%03d' % (ctr) + '.txt', 'w') as fid:
            for line in asciiTab:
                fid.write(line)
                fid.write('\n')

        arg.handles.pg_project.btnRecord.obj.config(text="Record and Save")
        
        arg.currentRecord = 'ascii' + '%03d' % (ctr) + '.txt'
        gui.showPage(arg, 'pg_record')
    
    
    


def mergeRecords(arg):

    if len(arg.records) <= 1:
        gui.msgbox(arg, "Two or more records are required.", "ok", "error")
        return
    
    userRsp = gui.msgbox(arg, "Merging will combine all records into one. Continue?", "yesno", "question")

    if not userRsp == "yes":
        return
    
    asciiText = [
        'e |-',
        'B |-',
        'G |-',
        'D |-',
        'A |-',
        'E |-',
    ]
    for record in arg.records:
        with open('database/' + arg.currentProject + '/' + record, 'r') as fid:
            lines = fid.readlines()
            for idx, line in enumerate(lines):
                asciiText[idx] += line[4:-1]

    for record in arg.records:
        os.remove('database/' + arg.currentProject + '/' + record)
    
    with open('database/' + arg.currentProject + '/' +'ascii000.txt', 'w') as fid:
        for line in asciiText:
            fid.write(line)
            fid.write('\n')
    
    gui.showPage(arg, "pg_project")
    gui.msgbox(arg, "Successfully merged records.", "ok", "info")


def btnExport(arg):

    selection = arg.handles.pg_project.records.obj.curselection()

    if len(selection) == 0:
        gui.msgbox(arg, "No record selected.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return
    
    if len(selection) > 1:
        gui.msgbox(arg, "Choose only one record.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return

    idx = selection[0]

    with open('database/' + arg.currentProject + '/' + arg.records[idx], 'r') as fid:
        lines = fid.readlines()

    # Measure Line Length
    lineLength = len(lines[0])

    numCharsPerRow = 55
    numRowsPerPage = 6

    # See how many rows to break into
    numRows = math.ceil(lineLength / numCharsPerRow)

    # See how many pages to break into
    numPages = math.ceil(numRows/numRowsPerPage)

    pdf = FPDF()

    for page in range(0,numPages):
        pdf.add_page()
        pdf.set_font('Courier', '', size=16)

        for rowPage in range(0,numRowsPerPage):
            row = rowPage + (page * numRowsPerPage) 

            pdfY = 10 + (rowPage * 45)
            for line in lines:
                pdf.set_x(10)
                pdf.set_y(pdfY)
                pdf.cell(100, 10, line[(numCharsPerRow * row):(numCharsPerRow * (row + 1))])
                pdfY += 6
    
    arg.currentRecord = arg.currentProject + '_' + arg.records[idx][0:-4] + '.pdf'
    
    if os.path.exists('exports/' + arg.currentRecord):
        os.remove('exports/' + arg.currentRecord)
        
    pdf.output('exports/' + arg.currentRecord, 'F')

    del pdf

    gui.showPage(arg, 'pg_pdf')

    # gui.msgbox(arg, "Succesfully exported PDF file.", "ok", "info")


def notesToAsciiTab(notes):

    string = [
        ['E4','F4','F#4','G4','G#4','A4','A#4','B4','C5','C#5','D5','D#5','E5','F5','F#5','G5','G#5','A5','A#5','B5'],
        ['B3','C4','C#4','D4','D#4'],
        ['G3','G#3','A3','A#3'],
        ['D3','D#3','E3','F3','F#3'],
        ['A2','A#2','B2','C3','C#3'],
        ['E2','F2','F#2','G2','G#2'],
    ]
    asciiText = [
        'e |-',
        'B |-',
        'G |-',
        'D |-',
        'A |-',
        'E |-',
    ]

    for note in notes:
        idxFound = False
        stringIdx = 0
        for idx in range(0,len(string)):
            if note in string[idx]:
                idxFound = True
                stringIdx = idx
                break
        
        if idxFound:
            fretNum = str(string[stringIdx].index(note))
            for idx in range(0,len(string)):
                if idx == stringIdx:
                    asciiText[idx] += fretNum + '-'
                else:
                    asciiText[idx] += '-' * (len(fretNum) + 1)
        else:
            for idx in range(0,len(string)):
                asciiText[idx] += '--'

    
    return asciiText

# https://stackoverflow.com/questions/64505024/turning-a-frequency-into-a-note-in-python
def frequency_to_note(frequency):
    
    # define constants that control the algorithm
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # these are the 12 notes in each octave
    OCTAVE_MULTIPLIER = 2 # going up an octave multiplies by 2
    KNOWN_NOTE_NAME, KNOWN_NOTE_OCTAVE, KNOWN_NOTE_FREQUENCY = ('A', 4, 440) # A4 = 440 Hz

    # calculate the distance to the known note
    # since notes are spread evenly, going up a note will multiply by a constant
    # so we can use log to know how many times a frequency was multiplied to get from the known note to our note
    # this will give a positive integer value for notes higher than the known note, and a negative value for notes lower than it (and zero for the same note)
    note_multiplier = OCTAVE_MULTIPLIER**(1/len(NOTES))
    frequency_relative_to_known_note = frequency / KNOWN_NOTE_FREQUENCY
    distance_from_known_note = math.log(frequency_relative_to_known_note, note_multiplier)

    # round to make up for floating point inaccuracies
    distance_from_known_note = round(distance_from_known_note)

    # using the distance in notes and the octave and name of the known note,
    # we can calculate the octave and name of our note
    # NOTE: the "absolute index" doesn't have any actual meaning, since it doesn't care what its zero point is. it is just useful for calculation
    known_note_index_in_octave = NOTES.index(KNOWN_NOTE_NAME)
    known_note_absolute_index = KNOWN_NOTE_OCTAVE * len(NOTES) + known_note_index_in_octave
    note_absolute_index = known_note_absolute_index + distance_from_known_note
    note_octave, note_index_in_octave = note_absolute_index // len(NOTES), note_absolute_index % len(NOTES)
    note_name = NOTES[note_index_in_octave]
    return note_name + str(note_octave)



def getFrequency(yCurrent, Fs, previous1Response=None, previous2Response=None):

    MAX_FREQ = 1200 # HZ
    BEFORE_RESPONSE_SUBTRACT_FACTOR_1 = 0.45
    BEFORE_RESPONSE_SUBTRACT_FACTOR_2 = 0.13
    MIN_RESPONSE = 1
    
    yfft = np.fft.fft(yCurrent)
    freqs = np.fft.fftfreq(len(yfft))

    # Get Only Positive Side
    toIdx = np.where(freqs * Fs > MAX_FREQ)[0][0]
    currentResponse = abs(yfft[0:toIdx])

    freqs = freqs[0:toIdx] * Fs

    # Subtract Portion of Previous Response 1
    if previous1Response is not None:
        newResponse = currentResponse - (previous1Response * BEFORE_RESPONSE_SUBTRACT_FACTOR_1)
    else:
        newResponse = currentResponse
    
    # Subtract Portion of Previous Response 2
    if previous2Response is not None:
        newResponse = newResponse - (previous2Response * BEFORE_RESPONSE_SUBTRACT_FACTOR_2)
    else:
        newResponse = newResponse


    # Weight Response By Frequency
    # Try Linear
    responseWeight = np.linspace(MIN_RESPONSE,1,len(newResponse))

    newResponse = newResponse * responseWeight

    newResponse[newResponse<0] = 0

    peakProminence = PEAK_PROMINENCE * max(newResponse)
    peaks = find_peaks(newResponse, prominence=peakProminence )[0].astype(int)
    # plt.plot(freqs, newResponse)
    # plt.show()

    idx = peaks[0]

    # # Get Maximum Response
    # idx = np.argmax(newResponse)
    
    freq_in_hertz = freqs[idx]

    return freq_in_hertz, currentResponse, previous1Response



def threadRecordAudio(arg):

    print("THREAD: RECORDING START")
    timeIn = time.time()

    with sf.SoundFile('currentRecording.wav', mode='w', samplerate=48000,
                        channels=1, subtype='PCM_24') as file:
        with sd.InputStream(samplerate=48000, device=1,
                                channels=1, callback=callback):
            while arg.trigRecording:

                file.write(q.get())

            # # loop through stream and append audio chunks to frame array
            # data = arg.stream.read(arg.chunk)
            # arg.frames.append(data)
    
    arg.recordState = False
    
    print("THREAD: RECORDING END")
    print("Recording Time:", time.time() - timeIn, 'seconds')



def deleteRecord(arg):
    selection = arg.handles.pg_project.records.obj.curselection()

    if len(selection) == 0:
        gui.msgbox(arg, "No record selected.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return
    
    if len(selection) == 1:

        idx = selection[0]
        userRsp = gui.msgbox(arg, 'Are you sure to delete record: "' + arg.records[idx] + '"?',
                MessageBoxButtons = "yesno",
                MessageBoxIcon = "question",
            )
        
        if not userRsp == 'yes':
            return
        
        os.remove('database/' + arg.currentProject + '/' + arg.records[idx])
    
    else:
        userRsp = gui.msgbox(arg, 'Are you sure to delete ' + str(len(selection)) + ' records?',
                MessageBoxButtons = "yesno",
                MessageBoxIcon = "question",
            )
        
        if not userRsp == 'yes':
            return
        
        for idx in selection:
            os.remove('database/' + arg.currentProject + '/' + arg.records[idx])


    gui.showPage(arg, 'pg_project')

