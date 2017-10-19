/* A little app that has a data set where the data is a pair:  
   a picture and a sound - and for implementation purposes 
   I need a name to identify the datum I am currently refering to.
   
   So I need a data folder that has a sequence of?
   Since I have a collection of folders (hmmm, why did I make you put is in folders,
   I can ITERATE through the names of the folders.
   
   PImage photo; // I declare a variable that is a PImage.
  photo = loadImage("laDefense.jpg");// I can specify a path name.
  
  How am I going to impement buttons?
  
  
}
*/

Person [] people = new Person[20];

// This is temporary, its just for testing //
String [] names = {"NIDESHCHITRAKAR","NATEGUEVIN","OLIVERWODUNNE"};
int currentPicture = 0;

void setup() {
   size(400,600);
   /* Set up the data structure for the pictures and sound files 
      We need an OBJECT!!!!!!
      The data structure will allow us to iterate over the objects.*/
   /* for each person in the array instantiate that person based on what?
      brute force would be to do this by hand... have a list of names here in the code.
      maybe have a file of file names?
      is there a way to get a directory listing?
      for now just create a sample string and try it out. 
    
    for(int i = 0; i < people.length; i++ ) {
      people[i] = new Person(names[i]);
    }
    
    This introduces the problem of just getting the list of names,
    which is where we are going to leave it!
    */
 

   
   /* Iterate on loading all the pictures and sound files....*/
     
   
   /* show the next button */
 //  showNextButton();
 
}
/*  for each person, displayPictureAndSound once the initial next button is pressed */


void displayPictureAndSound() {
  //  showNextPlayButton();
 //  showNextPicture();
} 
void showNextButton() {
  /* not sure how I want to do this yet.... for now maybe just
  look for a keypress */
}
/* Draw is only going to be implemented when the button tells it to. */
void draw() {
  image(photo, 0, 0);
}