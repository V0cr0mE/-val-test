from locust import HttpUser, task


class User(HttpUser):

    @task
    def get_pokemons_trainers(self):
        self.client.get("/trainers/1")
        self.client.get("/trainers/2")

    @task
    def get_battle(self):
        self.client.get("/pokemons/battle/1/3")
