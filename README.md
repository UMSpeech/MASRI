# MASRI
Maltese Automatic Speech Recognition

# About the project
Masri is a project at the [University of Malta](https://www.um.edu.mt) which developed the foundations for Automatic Speech Recognition for the Maltese Language. For more information about MASRI, visit our website https://www.um.edu.mt/projects/masri/

# Data
The following are datasets prepared in the [MASRI](https://www.um.edu.mt/projects/masri/) project. All data is released for non-commercial use. The table below summarises the size of each dataset with a download link. The characteristics of each dataset are described below.

## How to download
To download this data, please visit the [MASRI project web page](https://www.um.edu.mt/projects/masri/#data), check the terms and conditions, and retrieve the data.


## Training data

| Dataset | Size | Type |#female voices|#male voices|
|---------|------|------|------------|--------------|
|MASRI-Headset v2|6h39m|Read speech|13|12|
|MASRI-Farfield|9h37m|Read speech|13|12|
|MASRI-Booths|2h27m|Read speech|2|3|
|MASRI-MEP|1h17m|Spontaneous speech|4|2|
|MASRI-COMVO|7h29m|Read speech|59|88|
|MASRI-TUBE|13h17m|Spontaneous speech|13|39|
|MASRI-Synthetic|99h18m|Synthesized speech|105|105|

## Dev and test data
| Dataset | Size | Type |
|---------|------|------|
|MASRI-Dev|1h|Spontaneous speech|
|MASRI-Test|1h|Spontaneous speech|

### General data characteristics
All the dataset share the following characteristics
- Audio files are distributed in a 16khz@16bit mono format.
- Every audio file has an ID that is compatible with ASR engines such as 
  Kaldi and CMU-Sphinx.
- Transcriptions are lowercase. Unless otherwise stated below, no punctuation marks are permitted 
  except dashes (-) and apostrophes (') because these belong to the Maltese 
  orthography.

### MASRI-HEADSET (v2.0)
This is a clean version of the dataset first reported in [Mena et al (2020)](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.784.pdf). For this version, excessive silence was trimmed and clicks were suppressed. All audio files are shorter than 11 seconds.

Data was collected in the following fashion:
- All recordings were elicited using short text snippets, which were read in 
  a laboratory environment.
- Recordings were made using a Sennheiser PC-8 headset
- Participants were recruited from different geographical locations in the 
  Maltese islands, and were roughly evenly distributed for gender.

### MASRI-Farfield (MFC)
This dataset was collected in parallel with MASRI-HEADSET and has similar characteristics. However, the recordings were done using a microphone placed at a distance of approximately 2m from the speaker. 

### MASRI-Booths
This dataset was recorded from read prompts, with speakers in soundproof booths.

### MASRI-MEP
This corpus was created from recordings of the interventions of the Maltese
Members of the European Parliament.

### MASRI-COMVO
This corpus was created entirely from the validated recordings in Maltese 
found at the [Mozilla Common Voice Project](https://commonvoice.mozilla.org/mt), the Maltese version of which was launched as a result of a MASRI initiative. 
The recordings were downloaded in December 28th, 2020 at 5:20 am (Malta time). 
According to the Common Voice website, the corpus version is 6.1.

### MASRI-TUBE
The MASRI-TUBE CORPUS was created by the MASRI team in collaboration with the Universidad 
Nacional Autónoma de México (UNAM) through the Social Service Program 
"Desarrollo de Tecnologías del Habla", lead by the CIEMPIESS-UNAM Project
(www.ciempiess.org)

The MASRI-TUBE CORPUS was made out of YouTube videos belonging to the YouTube 
Channel of the [University of Malta](www.youtube.com/user/universityofmalta).

The transcriptions have been hand verified. The corpus is compiled in standard
Maltese orthography. Markers of speech disfluency, such as false starts and 
repetitions, were conserved in the transcriptions. Furthermore, wherever 
possible, partially uttered words as a result of stuttering and interruption 
were transcribed as actual Maltese words, for instance, the initial 
en- part-word from "enerġija" (energy) being transcribed as "għen" 
([he] helped). Dialectal and non-standard realizations of words, e.g. ħen 
versus ħin "time", were corrected to official orthography. 

Where multiple phonetic variants are acceptable in the Maltese lexicon 
(e.g. kuntrast versus kontrast for "contrast"), the transcription reflects 
the recorded phonetic realization. Other common non-standard realizations of 
the metathetic (qbija versus bqija "remainder") or epenthetic formation (bej' 
versus bejn "between") were corrected to official orthographic standards.


### MASRI-Synthetic
This corpus consists entirely of synthesized speech using a concatenative Text to Speech Engine created by CrimsonWing and distributed by the [Foundation for Information Technology Accessibility (FITA)](https://fitamalta.eu/). The main purpose of this corpus is for use in data augmentation of ASR systems. 

More information on the TTS system used is available [here](https://pdfs.semanticscholar.org/5e5a/25e34b3c351ba0e58211a5192535e9ddea06.pdf).

The dataset has the following characteristics:
-  All sentences were sourced from the [MLRS Korpus Malti v3.0](https://mlrs.research.um.edu.mt) and put in a single plain text file. The text 
   includes punctuation marks.
-  To facilitate the text processing, sentences are split to fit into lines 
   with 30 words only.
-  Punctuation marks and sentences including not UTF-8 characters are removed.
-  Sentences with foreign words and proper names were removed.
-  As the letters "c" and "y" do not really belong to the Maltese alphabet, 
   sentences including words with any of those letters were removed. This is 
   done to ensure that only Maltese words will be included in each sentence.
-  Using Python, the resulting sentences are now put into a simple list; so, 
   each element is a word.
-  Each word of the list is now taken one by one to produce text lines of 
   exactly 13 words. This process only generated 27,714 sentences of the 
   52,500 that constitute the whole corpus.
-  To produce the remaining sentences, the words of the list were shuffled 
   and the process in the previous point were repeated until we got the 
   52,500 sentences needed by the corpus.
-  At the end, the produced sentences were converted into utterances using the 
   TTS system.

### MASRI-Test

The MASRI-TEST CORPUS was created out of YouTube videos belonging to the
channel of the University of Malta. It has a length of 1 hour and it is 
gender balanced, as it has the same number of male and female speakers.

The MASRI-TEST CORPUS was possible due to a collaboration of two different 
Universities. The data selection and audio segmentation was 
performed by the CIEMPIESS-UNAM Project at the Universidad Nacional Autónoma
de México (UNAM) in Mexico City. The audio transcription and corpus edition 
was performed by the MASRI Team at the University of Malta in the Msida 
Campus.

### MASRI-DEV

The MASRI-DEV CORPUS was created out of YouTube videos belonging to the
channel of the University of Malta. It has a length of 1 hour and it is 
gender balanced, as it has the same number of male and female speakers.

The MASRI-DEV CORPUS was possible due to a collaboration of two different 
Universities. The data selection and audio segmentation was 
performed by the CIEMPIESS-UNAM Project at the Universidad Nacional Autónoma
de México (UNAM) in Mexico City. The audio transcription and corpus edition 
was performed by the MASRI Team at the University of Malta in the Msida 
Campus.



