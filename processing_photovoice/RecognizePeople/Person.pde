public class Person {
  PImage photo;
 
  void showImage(String name) {  // this is mine
     // Figure out which file type it is.
     
     photo = loadImage(name); // Is the Processing function
  }
  void draw() {
    image(photo, 0, 0);
  }
  
   // Needs sounds as well -- left as an exercise for the reader.....
}