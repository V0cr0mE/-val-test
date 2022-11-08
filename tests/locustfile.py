from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(2, 5)

    @task
    def get_trainers(self):
        self.client.get("/trainers")

    @task 
    def get_pokemons(self):
        self.client.get("/pokemons/")
    
    @task 
    def get_items(self):
        self.client.get("/items/")