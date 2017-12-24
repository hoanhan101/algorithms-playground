function Bullet(x, y) {
  this.x = x;
  this.y = y;
  this.radius = 8;
  this.didDelete = false;

  this.show = function() {
    noStroke();
    fill(253, 90, 232);
    rect(this.x, this.y, this.radius*2, this.radius*2);
  }

  this.disappear = function() {
    this.didDelete = true;
  }

  this.hits = function(enemy) {
    var distance = dist(this.x, this.y, enemy.x, enemy.y);
    if (distance < this.radius + enemy.radius) {
      return true;
    } else {
      return false;
    }
  }

  this.move = function() {
    this.y = this.y - 5;
  }

}
