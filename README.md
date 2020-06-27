# Deep Learning Pokedex

## Summary

This repository is just a simple hobbie project of a real life Pokedex using a Pytorch object detection model and a CSV with pokemon information.

## Process

The Training process of this project was really simple to do (and is not done yet) due to the tools used which made quite easy train an object detection model!

here we go:

1. LabelImg is being used to create the bounding boxes annotations, the advantage of use this tag tool is that it retrives the ground-truth in the Pascal Voc format which is used in most of Deep Learning frameworks making really easy the data preprocessing.
https://github.com/tzutalin/labelImg

2. Detecto is being used for both the training and inference part. Its a new package which makes the inference and training really intuitive/simple.
https://github.com/alankbi/detecto

So if you want to train an object detection model creating your own custom dataset i recommend this two repo.

## Model

The model is still in construction, so i will be updating this section depending on the training process and after de dataset is finish i will be providing also it!

The Pokemons are from the first generation and the ones supported are:
` ['Abra','Pikachu','Alakazam','Aerodactyl','Charizard','Bellsprout','Jiglypuff','Kadabra','Charmeleon','Dragonite','Raichu','Magmar','Jigglypuff','Eevee'\
    ,'Vaporeon','Jolteon','Grownlithe','Arcanine','Articuno','Arbok','Ekans','Flareon','Ditto'] `

download the last model here: https://drive.google.com/file/d/1dcTd4vDMvWDuOnagSfHf6bVMY4Iw5yCo/view?usp=sharing
and copy to `data` folder

## Usage

To use this repository please follow the steps below:

```
cd deep_learning_pokedex
python3.7 -m pip install -r requirements
python pokedex.py
```

After that just choose a video (also works with images) and click on the pokeball icon, if no video is choose the webcam will be used.