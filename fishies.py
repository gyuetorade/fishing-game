import random

fish = {
    'Banana': 'assets/Fish/Fishes/Banana.PNG',
    'Beluga Sturgeon': 'assets/Fish/Fishes/Beluga Sturgeon.png',
    'Box Jelly': 'assets/Fish/Fishes/BoxJelly.png',
    'Crab': 'assets/Fish/Fishes/Crab.png',
    'Dori': 'assets/Fish/Fishes/Dori.PNG',
    'Nemo': 'assets/Fish/Fishes/nemo.PNG',
    'Octopus': 'assets/Fish/Fishes/Octapus.PNG',
    'Orangeroughy': 'assets/Fish/Fishes/Orangeroughy.png',
    'Seahorse': 'assets/Fish/Fishes/Seahorse.png',
    'Shark': 'assets/Fish/Fishes/Shark.png',
    'Small tail shark': 'assets/Fish/Fishes/Small tail shark.png',
    'Squid': 'assets/Fish/Fishes/Squid.png',
    'Starfish': 'assets/Fish/Fishes/Starfish.PNG',
    'Stingray': 'assets/Fish/Fishes/Stingray.png',
    'Stingray with friends': 'assets/Fish/Fishes/Stingray with friends.png',
    'Tuna': 'assets/Fish/Fishes/Tuna.png',
}
def get_random_fish():
    return random.choice(list(fish.values()))