function Snake() {
  this.show = function() {
    fill(41, 252, 165);
    for(var i = 0; i < this.tail.length; i++) {
      rect(this.tail[i].x, this.tail[i].y, cellPixel, cellPixel);
    }
    rect(this.pos.x, this.pos.y, cellPixel, cellPixel)
  }

  this.update = function() {
    if(moves.length) {
      if(snake.speed.x != moves[0][0]*-1 && snake.speed.y != moves[0][1]*-1) {
        snake.changeDirection(moves[0][0], moves[0][1]);
      }
      moves.splice(0, 1);
    }

    this.tail.unshift(createVector(this.pos.x, this.pos.y));
    this.tail.pop();

    this.pos.x += this.speed.x * cellPixel;
    this.pos.y += this.speed.y * cellPixel;
  }

  this.changeDirection = function(x, y) {
    this.speed.x = x;
    this.speed.y = y;
  }

  this.checkIfDead = function() {
    if(this.pos.x >= width || this.pos.y >= height || this.pos.x < 0 || this.pos.y < 0) {
    	gameState = 'END';
    }
    for(var i = 0; i < this.tail.length; i++) {
      if(this.tail[i].x == this.pos.x && this.tail[i].y == this.pos.y) {
      	gameState = 'END';
      }
    }
  }

  this.eat = function(pos) {
    return this.pos.x == pos.x && this.pos.y == pos.y;
  }

  this.reset = function() {
    food = [];
    this.tail = [];
    this.pos = createVector(0, 0);
    this.speed = createVector(1, 0);
  }

  this.reset();
}
