// include gulp
var gulp = require('gulp');

// include JShint (mejora nuestro JS)
var jshint = require('gulp-jshint');
// checks for changes
var changed = require('gulp-changed');
// optimizes images for web development
var imagemin = require('gulp-imagemin');
// minifies css
var minifyCSS = require('gulp-minify-css');
// concatenates files
var concat = require('gulp-concat');
// minifies js
var uglify = require('gulp-uglify');
// removes console logs and debbuging tools from the code.
var stripDebug = require('gulp-strip-debug');

var stylish = require('jshint-stylish');


// check the quiality of my JS
gulp.task('jshint', function(){
	gulp.src('js/*.js')
	.pipe(jshint())
	.pipe(jshint.reporter(stylish))
});

// minify my css
gulp.task('styles', function(){
	gulp.src(['css/mystyle.css'])
	
	.pipe(minifyCSS())
	.pipe(gulp.dest('css/mystyle.min.css'))
});