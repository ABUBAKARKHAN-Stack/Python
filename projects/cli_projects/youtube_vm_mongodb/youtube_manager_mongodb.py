from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")

db = client["yt-manager"]

# db.create_collection("videos")
video_collection = db["videos"]


def list_videos():
    videos = video_collection.find()
    for video in videos:
        print(f"{video["_id"]}: 📺 Name: {video["name"]} | ⏱ Duration: {video["time"]}")


def add_video():
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    video_collection.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}}
    )


def delete_video(video_id):
    list_videos()
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:

        print("\nYoutube Manager App with MONGO DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            add_video()
        elif choice == "3":
            list_videos()
            video_id = input("Enter Video Id To Update: ")
            update_video(video_id)
        elif choice == "4":
            list_videos()
            video_id = input("Enter Video Id To Delete: ")
            delete_video(video_id)
        elif choice == "5":
            print("Exiting application...")
            break
        else:
            print("Invalid Choice!!")
    client.close()


if __name__ == "__main__":
    main()
