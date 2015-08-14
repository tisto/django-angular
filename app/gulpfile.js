(function() {
  'use strict';

  // --- DEPENDENCIES --------------------------------------------------------
  var gulp = require('gulp'),
      browserSync = require('browser-sync'),
      inject = require('gulp-inject'),
      sourcemaps = require('gulp-sourcemaps'),
      watch = require('gulp-watch');


  // --- INDEX ---------------------------------------------------------------
  gulp.task('index', function () {
    var target = gulp.src('./index.html');
    var sources = gulp.src([
      './node_modules/angular/angular.js',
      './node_modules/angular-mocks/angular-mocks.js',
      './node_modules/angular-loading-bar/build/loading-bar.js',
      './node_modules/underscore/underscore.js',
      './node_modules/restangular/dist/restangular.js',
      './node_modules/api-check/dist/api-check.js',
      './node_modules/angular-formly/dist/formly.js',
      './node_modules/angular-formly-templates-bootstrap/dist/angular-formly-templates-bootstrap.js',
      './js/**/*.js',
      './node_modules/angular-loading-bar/build/loading-bar.css',
      './node_modules/bootstrap/dist/css/bootstrap.css',
      './css/**/*.css'
    ], {read: false});  // Do not read the files, we're only after their paths.

    target.pipe(inject(sources))
      .pipe(gulp.dest('.'));
  });


  // --- JAVASCRIPT ----------------------------------------------------------
  gulp.task('js', function() {
    gulp.src('./js/**/*.js')
      .pipe(browserSync.reload({stream:true, once: true}));
  });


  // --- BROWSER SYNC --------------------------------------------------------
  gulp.task('browser-sync', function() {
    browserSync({
      server: {
        baseDir: "."
      }
    });
  });
  gulp.task('browser-sync-reload', function () {
    browserSync.reload();
  });


  // --- WATCH ---------------------------------------------------------------
  gulp.task('watch', function() {
    gulp.watch('./app/css/**/*.css', ['browser-sync-reload']);
    gulp.watch('./app/*.html', function(){
      gulp.run('index');
    });
    gulp.watch('./js/**/*.js', function(){
      gulp.run('js');
    });
  });


  // --- BUILD ---------------------------------------------------------------
  gulp.task('build', ['index'], function() {});


  // --- DEFAULT -------------------------------------------------------------
  gulp.task('default', ['build', 'watch', 'browser-sync'], function() {
    gulp.watch("*.*", ['browser-sync-reload']);
  });


})();
