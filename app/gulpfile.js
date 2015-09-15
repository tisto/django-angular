(function() {
  'use strict';

  // --- DEPENDENCIES --------------------------------------------------------
  var gulp = require('gulp');
  var browserSync = require('browser-sync');
  var inject = require('gulp-inject');
  var proxy = require('proxy-middleware');
  var sourcemaps = require('gulp-sourcemaps');
  var url = require('url');
  var watch = require('gulp-watch');


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
      './node_modules/angular-sanitize/angular-sanitize.min.js',
      './node_modules/tv4/tv4.js',
      './node_modules/objectpath/lib/ObjectPath.js',
      './node_modules/angular-schema-form/dist/schema-form.min.js',
      './node_modules/angular-schema-form/dist/bootstrap-decorator.min.js',
      './node_modules/angular-strap/dist/angular-strap.min.js',
      './node_modules/angular-strap/dist/angular-strap.tpl.min.js',
      './node_modules/schema-form-datetimepicker/schema-form-date-time-picker.js',
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
    var proxyOptions = url.parse('http://localhost:8000');
    proxyOptions.route = '/api';
    // requests to `/api/x/y/z` are proxied to `http://localhost:3000/secret-api`

    browserSync({
      server: {
        baseDir: ".",
        middleware: [proxy(proxyOptions)]
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
