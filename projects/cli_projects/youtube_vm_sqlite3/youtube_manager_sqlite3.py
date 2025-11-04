import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
    """
)



def list_videos():
    cursor.execute("SELECT * FROM videos")
    for idx,name,time in cursor.fetchall():
        print(f"{idx}. 📺 Name: {name} | ⏱ Duration: {time}")



def add_video():
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    cursor.execute("INSERT INTO videos (name ,time) VALUES (? , ?)", (name, time))
    conn.commit()


def update_video():
    list_videos()
    id = int(input("Enter Video Id To Update: "))
    name = input("Enter Video Name To Update: ")
    time = input("Enter Video Time: ")
    cursor.execute(
        "UPDATE videos SET name = ? , time = ? WHERE id = ?", (name, time, id)
    )
    conn.commit()



def delete_video():
    list_videos()
    id = int(input("Enter Video Id To Delete: "))
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    conn.commit()



def main():
    while True:

        print("\nYoutube Manager App with SQLITE3 DB")
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
            update_video()
        elif choice == "4":
            delete_video()
        elif choice == "5":
            print("Exiting application...")
            break
        else:
            print("Invalid Choice!!")
    conn.close()


if __name__ == "__main__":
    main()
