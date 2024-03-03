import random

fish = {
    'Banana': {'image': 'assets/Fish/Fishes/Banana.PNG', 'description': 'A yellow tropical fish with black stripes.', 'status': 'endangered'},
    'Beluga Sturgeon': {'image': 'assets/Fish/Fishes/BeLuga Sturgeon.png', 'description': 'A freshwater fish found in the Caspian and Black Seas, known for its large size and elongated snout. It is a bottom feeder with bony plates covering its body.,'},
    'Box Jelly': {'image': 'assets/Fish/Fishes/BoxJelly.PNG', 'description': 'A saltwater jellyfish found in the Indo-Pacific region, known for its box-shaped bell and venomous tentacles. It is a predator that floats in the water and stings its prey with its tentacles.'},
    'Crab': {'image': 'assets/Fish/Fishes/Crab.PNG', 'description': ' A saltwater or freshwater crustacean with ten legs and two claws, found in oceans, rivers, and on land. They have a hard exoskeleton and come in various shapes and sizes.'},
    'Blue Tang': {'image': 'assets/Fish/Fishes/Dori.PNG', 'description': 'Blue tang, A saltwater fish found in the Indo-Pacific region, known for its vibrant blue color, wide smile, and forgetful personality. It is a small, herbivorous fish that lives in coral reefs. '},
    'Octopus': {'image': 'assets/Fish/Fishes/Octopus.PNG', 'description': ' A saltwater mollusk with eight long arms and no bones, found in oceans worldwide. They are intelligent creatures with good camouflage abilities and can squeeze through small openings.', 'status': 'endangered'},
    'Orangeroughy': {'image': 'assets/Fish/Fishes/Banana.PNG', 'description': 'A saltwater fish found in deep, cool waters of the Atlantic, Pacific, and Indian Oceans. It is a commercially important fish with orange-rough skin and a large head.', 'status': 'endangered'},
    'Seahorse': {'image': 'assets/Fish/Fishes/Seahorse.PNG', 'description': 'A saltwater fish found in shallow, tropical and temperate waters. They have a unique body shape resembling a horses head and neck, and they coil their tails around underwater objects to anchor themselves.', 'status': 'endangered'},
    'Seal': {'image': 'assets/Fish/Fishes/Seal.PNG', 'description': 'A semi-aquatic mammal found in cold and temperate waters around the world. They have streamlined bodies, flippers, and thick fur, and they spend a lot of time on land but return to water to hunt.', 'status': 'endangered'},
    'Shark': {'image': 'assets/Fish/Fishes/Shark.PNG', 'description': 'A saltwater fish found in all oceans except the Arctic. They have a cartilaginous skeleton, sharp teeth, and powerful jaws. There are many different shark species, varying greatly in size and behavior.', 'status': 'endangered'},
    'Small tail shark':{'image': 'assets/Fish/Fishes/Small tail shark.PNG', 'description': 'Also known as a dogfish shark, it is a small saltwater shark found in deep waters around the world. They have a long, slender body and two small dorsal fins near the tail.', 'status': 'endangered'},
    'Squid': {'image': 'assets/Fish/Fishes/Squid.PNG', 'description': 'A saltwater mollusk with eight arms and two long tentacles, found in oceans worldwide. They are intelligent creatures with good camouflage abilities and jet-propel themselves through the water.', 'status': 'endangered'},
    'Starfish': {'image': 'assets/Fish/Fishes/Starfish.PNG', 'description': 'A saltwater echinoderm with five arms or more, found in all oceans from the tidal zone to deep waters. They have a central disc and a rough, bumpy texture on their bodies.', 'status': 'endangered'},
    'Stingray': {'image': 'assets/Fish/Fishes/Stingray.PNG', 'description': 'A saltwater fish with a flat, diamond-shaped body and a long, whip-like tail, found in shallow coastal waters around the world. Some stingrays have venomous barbs on their tails for defense.', 'status': 'endangered'},
    'Stingray with friends': {'image': 'assets/Fish/Fishes/Stingray with fvriends.PNG', 'description': 'A group of sea creatures', 'status': 'endangered'},
    'Sunfish': {'image': 'assets/Fish/Fishes/Sunfish.PNG', 'description': 'A saltwater fish found in all oceans except the Arctic. They are the heaviest bony fish in the world, with large, round bodies and fins.', 'status': 'endangered'},
    'Turtle': {'image': 'assets/Fish/Fishes/Turtle.PNG', 'description': 'A reptile found in both saltwater and freshwater habitats around the world. They have a hard shell that protects them from predators, and they lay their eggs on land.', 'status': 'endangered'},
    'Tuna':{'image': 'assets/Fish/Fishes/Tuna.PNG', 'description': 'A saltwater fish found in warm and temperate waters around the world. They are large, fast-swimming fish with streamlined bodies and are commercially important.', 'status': 'endangered'},
}


def get_random_fish():
    return random.choice(list(fish.values()))
