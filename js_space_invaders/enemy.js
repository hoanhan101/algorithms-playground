function Enemy(x, y) {
  this.x = x;
  this.y = y;
  this.radius = 20;
  this.didDelete = false;

  this.xdir = 1;

  this.grow = function() {
    this.radius = this.radius + 2;
  }

  this.disappear = function() {
    this.didDelete = true;
  }

  this.shiftDown = function() {
    this.xdir *= -1;
    this.y += this.radius;
  }

  this.move = function() {
    this.x = this.x + this.xdir;
  }

  this.show = function() {
    noStroke();
    fill(90, 232, 253);
    rect(this.x, this.y, this.radius*2, this.radius*2);
  }

}
