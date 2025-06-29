# 🗓️ Event Scheduler System

A RESTful backend system built using **Python 3.x** and **Flask** for managing scheduled events. It supports full CRUD operations with persistent storage in a JSON file.

---

## 🚀 Features

- Create, view, update, delete events
- Sort events by start time
- REST API tested via Postman
- Persistent local storage in `events.json`

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/event-scheduler.git
cd event-scheduler
```

2. Create & Activate Virtual Environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Create events.json
Create an empty file named events.json and add:

[]

▶️ Run the Application:

python app.py

Output:
* Running on http://127.0.0.1:5000/

📮 API Usage (Postman)
✅ Create Event
POST /events
Body (raw → JSON):

{
  "title": "Morning Standup",
  "description": "Daily sync",
  "start_time": "2025-07-01T09:00:00",
  "end_time": "2025-07-01T09:30:00"
}

Response:

{
  "message": "Event created",
  "event": {
    "id": "generated-uuid",
    ...
  }
}

📃 View All Events
GET /events
Sorted by start_time.

✏️ Update Event
PUT /events/<event_id>
Body:
{
  "title": "Updated Title"
}

❌ Delete Event
DELETE /events/<event_id>

✅ Sample Output (GET /events)
[
  {
    "id": "a7d...c7",
    "title": "Morning Standup",
    "description": "Daily sync",
    "start_time": "2025-07-01T09:00:00",
    "end_time": "2025-07-01T09:30:00"
  }
]

📦 Dependencies
Flask

pip install Flask

🌐 GitHub Repository
👉 https://github.com/yourusername/event-scheduler ← (Replace with your actual link)


