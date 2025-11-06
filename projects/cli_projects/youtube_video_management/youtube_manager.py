import json


file_name = "youtube.json"


def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n" + "=" * 35 + " 🎬 List Of All Videos " + "=" * 35)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. 📺 Name: {video['name']} | ⏱ Duration: {video['time']}")
    print("=" * 93 + "\n")


def add_video(videos):
    print("\n➕ Add a New Video")
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("✅ Video added successfully!")


def update_video(videos):
    print("\n✏️ Update Video Details")
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
        print("✅ Video updated successfully!")
    else:
        print("❌ Invalid Index Selected")


def delete_video(videos):
    print("\n🗑️ Delete a Video")
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("✅ Video deleted successfully!")
    else:
        print("❌ Invalid Index Selected")


def main():
    videos = load_data()
    while True:
        print("\n" + "=" * 30)
        print("🎥 YOUTUBE MANAGER 🎥")
        print("=" * 30)
        print("1️⃣  List all favourite videos")
        print("2️⃣  Add a youtube video")
        print("3️⃣  Update a youtube video details")
        print("4️⃣  Delete a youtube video")
        print("5️⃣  Exit the app")
        choise = input("Enter your choice: ")

        match choise:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("\n👋 Exiting the application... Goodbye!\n")
                break
            case _:
                print("⚠️ Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()