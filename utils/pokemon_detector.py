import cv2
from detecto.core import Model
from utils.labels import labels
import pandas as pd
import numpy as np


colors = {"Fire": (0, 0, 255), "Water": (255, 0, 0), "Ice": (
        239, 255, 0), "Bug": (0, 255, 162), "Fairy": (255, 144, 255), "Electric": (0, 205, 255),
        "Ghost": (122, 37, 34), "Dragon": (176, 76, 73), "Fighting": (0, 75, 150), "Flying": (255,151,112),
        "Grass": (0,255,0), "Ground": (135,184,222), "Steel": (151,152,152), "Normal": (182,182,182), 
        "Poison": (129,16,122), "Psychic": (141,47,223), "Rock": (90,154,203), "Dark": (8,35,55)}
class PokemonDetector:

    def __init__(self):
        self.model = Model.load("data/poke_detector.pth", labels)
        self.pokemon_list = pd.read_csv("data/pokemon.csv")

    def detect_pokemons(self, frame):
        predictions = self.model.predict(frame)
        for label, box, score in zip(*predictions):
            if score < 0.5:
                continue
            PokemonDetector.draw_pokemon_detected(self, frame , label, box)
            # # Create the box around each object detected
            # # Parameters: frame, (start_x, start_y), (end_x, end_y), (r, g, b), thickness
            # cv2.rectangle(frame, (box[0], box[1]),
            #               (box[2], box[3]), (255, 0, 0), 3)

            # # Write the label and score for the boxes
            # # Parameters: frame, text, (start_x, start_y), font, font scale, (r, g, b), thickness
            # cv2.putText(frame, '{}: {}'.format(label, round(score.item(), 2)), (box[0], box[1] - 10),
            #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    def draw_pokemon_detected(self, frame, label, box):
        width_perc = (box[2] - box[0])*0.5
        height_perc = (box[3] - box[1])*0.32

        pokemon = self.pokemon_list.loc[self.pokemon_list['Name'] == label].iloc[[0]]
        cv2.rectangle(frame, (box[0], box[1]),
                          (box[2], box[3]), colors[pokemon["Type 1"].item()], 2)
        cv2.rectangle(frame, (box[0], box[1]+((box[3] - box[1])-height_perc)),
                          (box[0]+width_perc,box[1]+(box[3] - box[1])), (255,255,255), cv2.FILLED)
        cv2.rectangle(frame, (box[0], box[1]+((box[3] - box[1])-height_perc)),
                          (box[0]+width_perc,box[1]+(box[3] - box[1])), colors[pokemon["Type 1"].item()], 2)
        # Draw pokemon name
        cv2.putText(frame, ("#"+ str(pokemon["#"].item())+ " " + pokemon["Name"].item()), (box[0]+(3*(width_perc/112.69)),box[1]+((box[3] - box[1])-height_perc+(11*(height_perc/42)))),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4*(width_perc/112.69), (0, 0, 0), 1)
        # # Draw Pokemon Type 1
        cv2.putText(frame, ("Type: "), (box[0]+(3*(width_perc/112.69)),box[1]+((box[3] - box[1])-height_perc+(25*(height_perc/42)))),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4*(width_perc/112.69), (0, 0, 0), 1)
        cv2.putText(frame, pokemon["Type 1"].item(), (box[0]+(35*(width_perc/112.69)),box[1]+((box[3] - box[1])-height_perc+(25*(height_perc/42)))),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4*(width_perc/112.69),  colors[pokemon["Type 1"].item()], 1)
        # # Draw Pokemon Type 2
        cv2.putText(frame, ("Type: "), (box[0]+(3*(width_perc/112.69)),box[1]+((box[3] - box[1])-height_perc+(39*(height_perc/42)))),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4*(width_perc/112.69), (0, 0, 0), 1)
        if not pd.isna(pokemon["Type 2"].item()):
            cv2.putText(frame, pokemon["Type 2"].item(), (box[0]+(35*(width_perc/112.69)),box[1]+((box[3] - box[1])-height_perc+(39*(height_perc/42)))),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4*(width_perc/112.69),  colors[pokemon["Type 2"].item()], 1)