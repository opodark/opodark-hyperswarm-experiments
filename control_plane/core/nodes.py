from datetime import datetime, timedelta

class Node:

    def __init__(self, node_id, meta):

        self.node_id = node_id
        self.meta = meta

        self.status = "new"
        self.last_seen = datetime.utcnow()

    def heartbeat(self):

        self.last_seen = datetime.utcnow()
        self.status = "online"

    def is_dead(self):

        return datetime.utcnow() - self.last_seen > timedelta(seconds=30)