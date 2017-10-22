import processing.sound.*;

PImage myImg;
SoundFile filename;

void setup() {
  size(640,640);
  myImg = loadImage("HoanhAn.jpg"); 
  filename = new SoundFile(this, "HoanhAn.mp3");
}

void draw() {
  image(myImg,0,0);
}

void mouseClicked() {
  filename.play();
}