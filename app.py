from flask import Flask, request, jsonify
import json, uuid, os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'events.json'

# Load data
def load_events():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save data
def save_events(events):
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=4)

# Create event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    event = {
        "id": str(uuid.uuid4()),
        "title": data['title'],
        "description": data['description'],
        "start_time": data['start_time'],  # ISO 8601 format expected
        "end_time": data['end_time']
    }
    events = load_events()
    events.append(event)
    save_events(events)
    return jsonify({"message": "Event created", "event": event}), 201

# List events
@app.route('/events', methods=['GET'])
def list_events():
    events = sorted(load_events(), key=lambda e: e['start_time'])
    return jsonify(events)

# Update event
@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    events = load_events()
    for e in events:
        if e['id'] == event_id:
            e['title'] = data.get('title', e['title'])
            e['description'] = data.get('description', e['description'])
            e['start_time'] = data.get('start_time', e['start_time'])
            e['end_time'] = data.get('end_time', e['end_time'])
            save_events(events)
            return jsonify({"message": "Event updated", "event": e})
    return jsonify({"error": "Event not found"}), 404

# Delete event
@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events()
    new_events = [e for e in events if e['id'] != event_id]
    if len(new_events) == len(events):
        return jsonify({"error": "Event not found"}), 404
    save_events(new_events)
    return jsonify({"message": "Event deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
