var snake;
var cellPixel = 20;
var food = [];
var moves = [];
var highScore = 100;
var gameState = 'START';

function setup() {
  createCanvas(600, 600);
  frameRate(10);
}

function init() {
  background(51);
  fill(41, 252, 165);
	var title = 'Snake';
	textSize(50);
  fill(41, 252, 165);
	nameWidth = textWidth(title);
	text(title, (width - nameWidth) / 2, height / 2 - 40);
	startBtn = createButton('Start');
	startBtn.position(width / 2 - startBtn.width / 2, height / 2);
	startBtn.mousePressed(startGame);
	noLoop();
}

function startGame() {
	removeElements();
	gameState = 'PLAYING';
	snake = new Snake();
	generateRandomFood(5);
	loop();
}

function runGame() {
	background(0);
	textSize(12);
  fill(90, 232, 253);
	text("score: " + snake.tail.length, 1, 10);
  fill(253, 90, 232);
	text("highScore: " + highScore, 1, 24);

	snake.update();
	snake.show();
	snake.checkIfDead();

	fill(255);
	for(var i = 0; i < food.length; i++) {
		rect(food[i].x, food[i].y, cellPixel, cellPixel);
		if(snake.eat(food[i])) {
			snake.tail.push(createVector(snake.x, snake.y));
			food.splice(i, 1);
			generateRandomFood(1);
			if(snake.tail.length > highScore) highScore = snake.tail.length;
		}
	}
}

function endGame() {
	background(51);
	textSize(32);
	var message = 'Game Over';
	var score = 'Your Score is ' + snake.tail.length;
	messageWidth = textWidth(message);
	scoreWidth = textWidth(score);
	fill(255);
	text(message, (width - messageWidth) / 2, height / 2 - 40);
	text(score, (width - scoreWidth) / 2, height / 2);
	startBtn = createButton('Restart');
	startBtn.position(width/2 - startBtn.width/2, height/2 + 40);
	startBtn.mousePressed(startGame);
	noLoop();
}

function draw() {
	if(gameState == 'START'){
		init();
	}
	else if(gameState == 'PLAYING') {
		runGame();
	}
	else if(gameState == 'END') {
		endGame();
	}
}

function generateRandomFood(num) {
  var cols = floor(width / cellPixel);
  var rows = floor(height / cellPixel);
  for(var i = 0; i < num; i++) {
    var location = createVector(floor(random(cols)), floor(random(rows))).mult(cellPixel);
    while(checkCollision(location)) {
      location = createVector(floor(random(cols)), floor(random(rows))).mult(cellPixel);
    }
    food.push(location);
  }
}

function checkCollision(location) {
  var didIntersect = false;
  if(location.x == snake.pos.x && location.y == snake.pos.y) {
    didIntersect = true;
  } else{
    for(var i = 0; i < snake.tail.length; i++) {
      if(location.x == snake.tail[i].x && location.y == snake.tail[i].y) {
        didIntersect = true;
        break;
      }
    }
    for(var i = 0; i < food.length; i++) {
      if(location.x == food[i].x && location.y == food[i].y) {
        didIntersect = true;
        break;
      }
    }
  }
  return didIntersect;
}

function keyPressed() {
  if(keyCode === DOWN_ARROW) {
    moves.push([0, 1]);
  } else if(keyCode === UP_ARROW) {
    moves.push([0, -1]);
  } else if(keyCode === LEFT_ARROW) {
    moves.push([-1, 0]);
  } else if(keyCode === RIGHT_ARROW) {
    moves.push([1, 0]);
  }
}
