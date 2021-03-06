# This file contains all parameters of the project

# DNN Parameters
DNN_HIDDEN_LAYER_SIZE = [4096, 2048, 1024]
MAX_EPOCHS_TRAIN = 25

# Audio Parameters
SAMPLE_RATE_HZ = float(16e3)
WINDOW_LENGTH_MS = float(20)
WINDOW_STEP_MS = float(10)
assert ((WINDOW_LENGTH_MS/1000.0)*SAMPLE_RATE_HZ).is_integer() is True
assert ((WINDOW_STEP_MS/1000.0)*SAMPLE_RATE_HZ).is_integer() is True

WINDOW_SIZE_SAMPLES = int((WINDOW_LENGTH_MS / 1000.0) * SAMPLE_RATE_HZ)
WINDOW_STEP_SAMPLES = int((WINDOW_STEP_MS / 1000.0) * SAMPLE_RATE_HZ)

SIGNAL_LENGTH_SEC = 2.4
NUM_OF_SOURCES_IN_SIGNAL = 2
NUM_OF_TRAIN_SIGNALS = 800
NUM_OF_TEST_SIGNALS = 50

NUM_OF_DIRECTIONS = 36

INPUT_SIGNAL_RMS = 1e-2

# Cochleagram Parameters
CGRAM_MIN_FREQ = 80
CGRAM_MAX_FREQ = 5000
CGRAM_NUM_CHANNELS = 256
CGRAM_NOISE_TH_dB = -10

# Spectrogram Parameters
SGRAM_TYPE = 'STFT' #'CGRAM'
SGRAM_NOISE_TH_dB = -5
SGRAM_NUM_CHANNELS = int(WINDOW_SIZE_SAMPLES/2+1)

# MFCC Parameters
MFCC_NUM_COEFF = 31
MFCC_MIN_FREQ = CGRAM_MIN_FREQ
MFCC_MAX_FREQ = CGRAM_MAX_FREQ

# GFCC Parameters
GFCC_NUM_CHANNELS = 64
GFCC_NUM_COEFF = 31

# Folders
OUTPUT_FOLDER = r'..\Results'
BRIR_FILE = r'..\Database\BRIR\UniS_Anechoic_BRIR_16k.sofa'
TRAIN_SENTENCES_FOLDER = r'..\Database\Clean\Train_Data'
TEST_SENTENCES_FOLDER = r'..\Database\Clean\Test_Data'

# IBM Parameters
MIXED_IBM_IDENTIFICATION_TH = 1500

# Feature Parameters
SIZE_OF_FEATURE_VEC = (2 * MFCC_NUM_COEFF) + SGRAM_NUM_CHANNELS + SGRAM_NUM_CHANNELS + \
                      (4 * SGRAM_NUM_CHANNELS) + (2 * GFCC_NUM_COEFF)
USE_MONAURAL_FEATURES = True

def getSizeOfFeatureVec():
    if(USE_MONAURAL_FEATURES == True):
        size_of_feature_vec = (2 * MFCC_NUM_COEFF) + SGRAM_NUM_CHANNELS + SGRAM_NUM_CHANNELS + \
                              (4 * SGRAM_NUM_CHANNELS) + (2 * GFCC_NUM_COEFF)
    else:
        size_of_feature_vec = SGRAM_NUM_CHANNELS + SGRAM_NUM_CHANNELS + (4 * SGRAM_NUM_CHANNELS)

    return size_of_feature_vec
