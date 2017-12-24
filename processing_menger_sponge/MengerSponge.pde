float angle = 0; 

ArrayList<Box> sponge;
void setup() {
  size(600, 600, P3D); 

  sponge = new ArrayList<Box>();

  Box b = new Box(0, 0, 0, 200);
  sponge.add(b);
}
void mousePressed() {
  ArrayList<Box> next = new ArrayList<Box>();
  for (Box b : sponge) {
    ArrayList<Box> newBoxes = b.generate();
    next.addAll(newBoxes);
  }
  sponge = next;
}

void draw() {
  clear();
  background(0);
  stroke(255);
  noFill();
  lights();
  translate(width / 2, height / 2); 
  rotateX(angle);
  rotateY(angle * 0.4);
  rotateZ(angle * 0.1);

  for (Box b : sponge) {
    b.show();
  }
  angle += 0.01;
}