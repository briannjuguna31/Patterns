from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class MP3Player(MediaPlayer):
    def play(self):
        # Implement play logic for MP3 files
        print("Playing MP3 file...")

    def pause(self):
        # Implement pause logic for MP3 files
        print("Pausing MP3 file...")

    def stop(self):
        # Implement stop logic for MP3 files
        print("Stopping MP3 file...")


class MP4Player(MediaPlayer):
    def play(self):
        # Implement play logic for MP4 files
        print("Playing MP4 file...")

    def pause(self):
        # Implement pause logic for MP4 files
        print("Pausing MP4 file...")

    def stop(self):
        # Implement stop logic for MP4 files
        print("Stopping MP4 file...")

#Introducing Extensibility whenyou have new format


class AVIPlayer(MediaPlayer):
    def play(self):
        # Implement play logic for AVI files
        print("Playing AVI file...")

    def pause(self):
        # Implement pause logic for AVI files
        print("Pausing AVI file...")

    def stop(self):
        # Implement stop logic for AVI files
        print("Stopping AVI file...")


def main():
    media_file = "sample.mp3"  # or "sample.mp4" or "sample.avi"

    # Determine the file format and create the corresponding media player
    if media_file.endswith(".mp3"):
        player = MP3Player()
    elif media_file.endswith(".mp4"):
        player = MP4Player()
    elif media_file.endswith(".avi"):
        player = AVIPlayer()
    else:
        print("Unsupported file format.")
        return

    # Play the media file using the appropriate player
    player.play()
    player.pause()
    player.stop()


if __name__ == "__main__":
    main()
