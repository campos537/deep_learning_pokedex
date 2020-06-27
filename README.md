# Deep Learning Pokedex

## Summary

This repository is just a simple hobbie project of a real life Pokedex using a Pytorch object detection model and a CSV with pokemon information.

## Process

The Training process of this project was really simple to do (and is not done yet) due to the tools used which made quite easy train an object detection model!

here we go:

1. (LabelImg)[https://github.com/tzutalin/labelImg] is being used to create the bounding boxes annotations, the advantage of use this tag tool is that it retrives the ground-truth in the Pascal Voc format which is used in most of Deep Learning frameworks making really easy the data preprocessing.

2. (Detecto)[https://github.com/alankbi/detecto] is being used for both the training and inference part. Its a new package which makes the inference and training really intuitive/simple.

So if you want to train an object detection model creating your own custom dataset i recommend this two repo.

## Model

The model is still in construction, so i will be updating this section depending on the training process and after de dataset is finish i will be providing also it!

The Pokemons are from the first generation and the ones supported are:
` ['Abra','Pikachu','Alakazam','Aerodactyl','Charizard','Bellsprout','Jiglypuff','Kadabra','Charmeleon','Dragonite','Raichu','Magmar','Jigglypuff','Eevee'\
    ,'Vaporeon','Jolteon','Grownlithe','Arcanine','Articuno','Arbok','Ekans','Flareon','Ditto'] `

