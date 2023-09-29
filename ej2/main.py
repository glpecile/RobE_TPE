import tkinter as tk
from PIL import Image, ImageTk
import requests
import io

class PokemonCounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pokemon Counter App")

        self.pokemon_list = [
            {"name": "pikachu", "score": 0},
            {"name": "bulbasaur", "score": 0},
            {"name": "charmander", "score": 0},
            {"name": "squirtle", "score": 0},
        ]

        self.current_index = 0
        self.current_pokemon = self.pokemon_list[self.current_index]

        self.score_label = tk.Label(master, text=f"Score: {self.current_pokemon['score']}")
        self.score_label.pack()

        self.image_label = tk.Label(master)
        self.image_label.pack()

        like_button = tk.Button(master, text="Like", command=self.like)
        like_button.pack(side=tk.LEFT)

        dislike_button = tk.Button(master, text="Dislike", command=self.dislike)
        dislike_button.pack(side=tk.RIGHT)

        self.update_display()

    def like(self):
        self.current_pokemon['score'] += 1
        self.next_pokemon()
        self.update_display()

    def dislike(self):
        self.current_pokemon['score'] -= 1
        self.next_pokemon()
        self.update_display()

    def next_pokemon(self):
        self.current_index = (self.current_index + 1) % len(self.pokemon_list)
        self.current_pokemon = self.pokemon_list[self.current_index]

    def update_display(self):
        self.score_label.config(text=f"Score: {self.current_pokemon['score']}")

        # Fetch and display Pokemon image
        image_url = self.get_pokemon_image_url(self.current_pokemon['name'])
        image = self.load_image_from_url(image_url)
        self.image_label.config(image=image)
        self.image_label.image = image

    def get_pokemon_image_url(self, pokemon_name):
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
        response = requests.get(api_url)
        data = response.json()
        image_url = data['sprites']['front_default']
        return image_url

    def load_image_from_url(self, url):
        response = requests.get(url)
        img_data = response.content
        img = Image.open(io.BytesIO(img_data))
        img = ImageTk.PhotoImage(img)
        return img

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonCounterApp(root)
    root.mainloop()
