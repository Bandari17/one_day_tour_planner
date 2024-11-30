from neo4j import GraphDatabase

class MemoryAgent:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def store_user_preferences(self, username, preferences):
        with self.driver.session() as session:
            session.run("CREATE (u:User  {name: $name, preferences: $preferences})",
                        name=username, preferences=preferences)
