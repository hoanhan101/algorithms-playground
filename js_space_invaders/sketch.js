var ship;
var enemies = [];
var enemies1 = [];
var bullets = [];

function setup() {
  createCanvas(600, 600);
  ship = new Ship();
  for (var i = 0; i < 10; i++) {
    enemies[i] = new Enemy(i * 60, 60);
  }
}

function draw() {
  background(0);
  ship.show();
  ship.move();

  for (var i = 0; i < bullets.length; i++) {
    bullets[i].show();
    bullets[i].move();
    for (var j = 0; j < enemies.length; j++) {
      if (bullets[i].hits(enemies[j])) {
        enemies[j].disappear();
        bullets[i].disappear();
      }
    }
  }

  var didHitEdge = false;

  for (var i = 0; i < enemies.length; i++) {
    enemies[i].show();
    enemies[i].move();
    if (enemies[i].x > width || enemies[i].x < 0) {
      didHitEdge = true;
    }
  }

  if (didHitEdge) {
    for (var i = 0; i < enemies.length; i++) {
      enemies[i].shiftDown();
    }
  }

  for (var i = bullets.length-1; i >= 0; i--) {
    if (bullets[i].didDelete) {
      bullets.splice(i, 1);
    }
  }

  for (var i = enemies.length-1; i >= 0; i--) {
    if (enemies[i].didDelete) {
      enemies .splice(i, 1);
    }
  }


}

function keyReleased() {
  if (key != ' ') {
    ship.setDir(0);
  }
}


function keyPressed() {
  if (key === ' ') {
    var bullet = new Bullet(ship.x, height);
    bullets.push(bullet);
  }

  if (keyCode === RIGHT_ARROW) {
    ship.setDir(1);
  } else if (keyCode === LEFT_ARROW) {
    ship.setDir(-1);
  }
}
