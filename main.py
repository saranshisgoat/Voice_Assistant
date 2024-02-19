import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
import pyautogui
import webbrowser
import os

# Add the path to the FFmpeg bin directory
ffmpeg_path = r"C:\Users\smaha\Downloads\ffmpeg-2024-02-15-git-a2cfd6062c-full_build.7z\ffmpeg-2024-02-15-git-a2cfd6062c-full_build\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError as e:
        print(f"Unable to access the Google Speech Recognition API: {e}")
        return None



def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    ffmpeg_command = os.path.join(ffmpeg_path, "ffmpeg")  # Full path to ffmpeg executable
    os.system(f"{ffmpeg_command} -i response.wav -y response.mp3")  # Convert wav to mp3
    os.system("start response.mp3")


tasks = []
listening_to_task = False


def main():
    global tasks
    global listening_to_task
    respond("Hello, Saransh. I hope you're having a nice day today.")
    while True:
        command = listen_for_command()

        trigger_keyword = "smj"

        if command and trigger_keyword in command:
            if listening_to_task:
                tasks.append(command)
                listening_to_task = False
                respond("Adding " + command + " to your task list. You have " + str(len(tasks)) + "in your list.")
            elif "add a task" in command:
                listening_to_task = True
                respond("Sure, what is the task?")
            elif "list tasks" in command:
                respond("Sure. Your tasks are:")
                for task in tasks:
                    respond(task)
            elif "take a screenshot" in command:
                pyautogui.screenshot("screenshot.png")
                respond("I took a screenshot for you.")
            elif "open chrome" in command:
                respond("Opening Chrome.")
                webbrowser.open("https://www.instagram.com/saransh__999/")
            elif "exit" in command:
                respond("Goodbye!")
                break
            else:
                respond("Sorry, I'm not sure how to handle that command.")


if __name__ == "__main__":
    # print(listen_for_command())
    respond("SmJ is goat the best")
    #main()
