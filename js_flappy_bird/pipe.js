function Pipe() {
  var spacing = random(50, height / 2);
  var centerY = random(spacing, height - spacing);

  this.top = centerY - spacing / 2;
  this.bottom = height - (centerY + spacing / 2);
  this.x = width;
  this.w = 30;
  this.speed = 2;

  this.highlight = false;

  this.hits = function(bird) {
    if (bird.y < this.top || bird.y > height - this.bottom) {
      if (bird.x > this.x && bird.x < this.x + this.w) {
        this.highlight = true;
        return true;
      }
    }
    return false;
  }

  this.show = function() {
    fill(90, 232, 253);
    if (this.highlight) {
      fill(253, 90, 232);
    }
    rect(this.x, 0, this.w, this.top);
    rect(this.x, height-this.bottom, this.w, this.bottom);
  }

  this.update = function() {
    this.x -= this.speed;
  }

  this.offscreen = function() {
    if (this.x < -this.w) {
      return true;
    } else {
      return false;
    }
  }
}
