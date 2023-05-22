import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)

# List Models
    # print(openai.Model.list())
    # for model in openai.Model.list()['data']:
    # print(model['id'])

#To get details about a specific model 
    # openai.Model.retrieve("text-davinci-003")
    # print(openai.Model.retrieve("text-davinci-003"))

# To get model completion -- https://platform.openai.com/docs/models/model-endpoint-compatibility
#   response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
#   print(response) 

# Create chat completion  https://platform.openai.com/docs/api-reference/chat/create
#completion = openai.ChatCompletion.create(
#  model="gpt-3.5-turbo",
#  messages=[
#    {"role": "user", "content": ""}
#  ]
#)
#print(completion.choices[0].message)

# Edit -- Given a prompt and an instruction, the model will return an edited version of the prompt. https://platform.openai.com/docs/api-reference/edits
#edit = openai.Edit.create(
#  model="text-davinci-edit-001",
#  input="What day of the wek is it?",
#  instruction="Fix the spelling mistakes"
#)
#print(edit)

# Not working
#Image -- Creates an edited or extended image given an original image and a prompt.-- https://platform.openai.com/docs/api-reference/images/create-edit
#editedimage = openai.Image.create_edit(
#  image=open("sample.png", "rb"),
#  mask=open("sample.png", "rb"),
#  prompt="A cute baby sea otter wearing a beret"
#)
#print(editedimage)

# Not working
# Image -- creates image variation
#openai.Image.create_variation(
# openai.Image.create_variation(
#  image=open("sample.png", "rb"),
#  n=2,
#  size="1024x1024"
#)
#)
#print(image)


#Embdeding -- Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms. -- https://platform.openai.com/docs/api-reference/embeddings
#embededReturn = openai.Embedding.create(
#  model="text-embedding-ada-002",
#  input="The food was delicious and the waiter..."
#)
#print(embededReturn)


# Transcription -- Transcribes audio into the input language. -- https://platform.openai.com/docs/api-reference/audio/create
# Spanish
#audio_file = open("Spanish.mp3", "rb")
#transcrib = openai.Audio.transcribe("whisper-1", audio_file, language ="es" )
#print(transcrib)

#hindi
#audio_file = open("Hindi.mp3", "rb")
#transcrib = openai.Audio.transcribe("whisper-1", audio_file, language ="hi", response_format = "text" )
#print(transcrib)

# Trnaslation -- Translates audio into into English. -- https://platform.openai.com/docs/api-reference/audio/create
#audio_file = open("Spanish.mp3", "rb")
#transcript = openai.Audio.translate("whisper-1", audio_file, response_format = "text")
#print(transcript)

#Files

# List files that belong to the user's organization. -- https://platform.openai.com/docs/api-reference/files/list
#listOfFiles = openai.File.list()
#print(listOfFiles)

# File upload - https://platform.openai.com/docs/api-reference/files/upload
#openai.File.create(
#file=open("cnn_dailymail_data_prepared_valid.jsonl", "rb"),
#   purpose='fine-tune'
#)

#Delete File -- https://platform.openai.com/docs/api-reference/files/delete
#openai.File.delete("file-ID")

#Retrieve File - https://platform.openai.com/docs/api-reference/files/retrieve
#openai.File.retrieve("file-ID")

#Retrieve file content -- https://platform.openai.com/docs/api-reference/files/retrieve-content
#content = openai.File.download("file-ID")
#print(content)

# Fine tune -- Create -- https://platform.openai.com/docs/api-reference/fine-tunes/create
#fineTuneCreate = openai.FineTune.create(training_file="file-ID")
#print(fineTuneCreate)

# Fine Tune List -- https://platform.openai.com/docs/api-reference/fine-tunes/list
#fineTuneList = openai.FineTune.list()
#print(fineTuneList)

#Retrieve Fine Tune job -- https://platform.openai.com/docs/api-reference/fine-tunes/retrieve
#openai.FineTune.retrieve(id="ft-AF1WoRqd3aJAHsqc9NY7iL8F")

# Can fine-tune job -- https://platform.openai.com/docs/api-reference/fine-tunes/cancel
#openai.FineTune.cancel(id="ft-AF1WoRqd3aJAHsqc9NY7iL8F")

#List fine tune events -- Get fine-grained status updates for a fine-tune job. -- https://platform.openai.com/docs/api-reference/fine-tunes/events
#openai.FineTune.list_events(id="ft-AF1WoRqd3aJAHsqc9NY7iL8F")

# Delete a fine tune moel -- need owner role at org level -- https://platform.openai.com/docs/api-reference/fine-tunes/delete-model
#openai.Model.delete("curie:ft-acmeco-2021-03-03-21-44-20")

#Moderation -- lassifies if text violates OpenAI's Content Policy -- https://platform.openai.com/docs/api-reference/moderations/create
#classified = openai.Moderation.create(input="I want to kill them.",)
#print(classified)

