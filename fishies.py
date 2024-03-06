import random

fishes = [
    {
        'name': 'Anchovy ',
        'image': 'assets/Fish/Fishes/Anchovy.png',  # Adjust the path as needed
        'description': ' A saltwater fish known for its small size and strong flavor. Anchovies are often used in various cuisines and are commonly found in temperate waters. They have a slender, silvery body and are an important part of marine ecosystems.',
        'endangered': False
    },
    {
        'name': 'Beluga Sturgeon ',
        'image': 'assets/Fish/Fishes/BelugaSturgeon.png',
        'description': ' A freshwater fish found in the Caspian and Black Seas, known for its large size and elongated snout. It is a bottom feeder with bony plates covering its body.',
        'endangered': True
    },
    {
        'name': 'Box Jelly ',
        'image': 'assets/Fish/Fishes/BoxJelly.PNG',
        'description': ' A saltwater jellyfish found in the Indo-Pacific region, known for its box-shaped bell and venomous tentacles. It is a predator that floats in the water and stings its prey with its tentacles.',
        'endangered': False
    },
    {
        'name': 'Crab ',
        'image': 'assets/Fish/Fishes/Crab.PNG',
        'description': ' A saltwater or freshwater crustacean with ten legs and two claws, found in oceans, rivers, and on land. They have a hard exoskeleton and come in various shapes and sizes.',
        'endangered': False
    },
    {
        'name': 'Blue Tang ',
        'image': 'assets/Fish/Fishes/Dori.PNG',
        'description': ' A saltwater fish found in the Indo-Pacific region, known for its vibrant blue color, wide smile, and forgetful personality. It is a small, herbivorous fish that lives in coral reefs.',
        'endangered': False
    },
    {
        'name': 'Clownfish ',
        'image': 'assets/Fish/Fishes/Nemo.PNG',
        'description': ' Also known as a Nemo, it is a saltwater fish found in the warm waters of the Indian Ocean, including the Red Sea. It lives among the tentacles of sea anemones for protection and has distinctive orange and white stripes.',
        'endangered': False
    },
    {
        'name': 'Octopus ',
        'image': 'assets/FIsh/Fishes/Octopus.PNG',
        'description': ' A saltwater mollusk with eight long arms and no bones, found in oceans worldwide. They are intelligent creatures with good camouflage abilities and can squeeze through small openings.',
        'endangered': True
    },
    {
        'name': 'Orangeroughy ',
        'image': 'assets/Fish/Fishes/Orangeroughy.PNG',
        'description': ' A saltwater fish found in deep, cool waters of the Atlantic, Pacific, and Indian Oceans. It is a commercially important fish with orange-rough skin and a large head.',
        'endangered': True
    },
    {
        'name': 'Seahorse',
        'image': 'assets/Fish/Fishes/Seahorse.PNG',
        'description': ' A saltwater fish found in shallow, tropical and temperate waters. They have a unique body shape resembling a horse\'s head and neck, and they coil their tails around underwater objects to anchor themselves.',
        'endangered': True
    },
    {
        'name': 'Seal',
        'image': 'assets/Fish/Fishes/Seal.PNG',
        'description': ' A semi-aquatic mammal found in cold and temperate waters around the world. They have streamlined bodies, flippers, and thick fur, and they spend a lot of time on land but return to water to hunt.',
        'endangered': True
    },
    {
        'name': 'Shark',
        'image': 'assets/Fish/Fishes/Shark.PNG',
        'description': ' A saltwater fish found in all oceans except the Arctic. They have a cartilaginous skeleton, sharp teeth, and powerful jaws. There are many different shark species, varying greatly in size and behavior.',
        'endangered': True
    },
    {
        'name': 'Smalltail Shark',
        'image': 'assets/Fish/Fishes/Small_tail_shark.PNG',
        'description': ' Also known as a dogfish shark, it is a small saltwater shark found in deep waters around the world. They have a long, slender body and two small dorsal fins near the tail.',
        'endangered': True
    },
    {
        'name': 'Squid',
        'image': 'assets/Fish/Fishes/Squid.PNG',
        'description': ' A saltwater mollusk with eight arms and two long tentacles, found in oceans worldwide. They are intelligent creatures with good camouflage abilities and jet-propel themselves through the water.',
        'endangered': False
    },
    {
        'name': 'Starfish',
        'image': 'assets/Fish/Fishes/Starfish.PNG',
        'description': ' A saltwater echinoderm with five arms or more, found in all oceans from the tidal zone to deep waters. They have a central disc and a rough, bumpy texture on their bodies.',
        'endangered': False
    },
    {
        'name': 'Stingray',
        'image': 'assets/Fish/Fishes/Stingray.PNG',
        'description': ' A saltwater fish with a flat, diamond-shaped body and a long, whip-like tail, found in shallow coastal waters around the world. Some stingrays have venomous barbs on their tails for defense.',
        'endangered': False
    },
    {
        'name': 'Sunfish',
        'image': 'assets/Fish/Fishes/Sunfish.PNG',
        'description': ' A saltwater fish found in all oceans except the Arctic. They are the heaviest bony fish in the world, with large, round bodies and fins.',
        'endangered': False
    },
    {
        'name': 'Swordfish',
        'image': 'assets/Fish/Fishes/Swordfish.PNG',
        'description': ' A saltwater fish found in tropical and temperate waters around the world. They are large, fast-swimming fish with a long, pointed bill used for hunting prey.',
        'endangered': False
    },
    {
        'name': 'Turtle',
        'image': 'assets/Fish/Fishes/Turtle.png',
        'description': ' A reptile found in both saltwater and freshwater habitats around the world. They have a hard shell that protects them from predators, and they lay their eggs on land.',
        'endangered': True
    },
    {
        'name': 'Tuna',
        'image': 'assets/Fish/Fishes/Tuna.png',
        'description': ' A saltwater fish found in warm and temperate waters around the world. They are large, fast-swimming fish with streamlined bodies and are commercially important.',
        'endangered': True
    },
    {
        'name': 'Sea Lion',
        'image': 'assets/Fish/Fishes/Sea_lion.PNG',
        'description': ' A semi-aquatic mammal found in the cold waters of the Pacific and Atlantic Oceans. They are social animals with large flippers for swimming and spend time on land to rest and breed.',
        'endangered': False
    }
]
def get_random_fish():
    return random.choice(fishes)


