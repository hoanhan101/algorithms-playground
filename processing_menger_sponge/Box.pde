class Box {
  PVector position; 
  float r; //size of box

  Box(float x, float y, float z, float r_) {
    position = new PVector(x, y, z);
    r = r_;
  }

  ArrayList<Box> generate() {
    ArrayList<Box> boxes = new ArrayList<Box>();
    for (int x = -1; x < 2; x++) {
      for (int y = -1; y < 2; y++) {
        for (int z = -1; z < 2; z++) {
          // if the sum of any two of axes is 0, the box associated should be remove
          int sum = abs(x) + abs(y) + abs(z);  
          float newR = r/3;

          //therefore, only create the box if sum is greater than 1
          if (sum > 1) {
            Box b = new Box(position.x + x*newR, position.y + y*newR, position.z + z*newR, newR);
            boxes.add(b);
          }
        }
      }
    }
    return boxes;
  }

  void show() {
    pushMatrix();
    translate(position.x, position.y, position.z);
    noStroke();
    fill(41, 252, 165);
    box(r);
    popMatrix();
  }
}