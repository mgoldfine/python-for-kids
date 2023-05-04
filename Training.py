
suits = ["пики", "бубны", "черви", "крести"]
faces = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
suits_and_faces = []
for suit in suits:
    for face in faces:
        suit_and_face = [face, suit]
        suits_and_faces.append(suit_and_face)
print(suits_and_faces)
