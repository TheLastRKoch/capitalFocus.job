<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');

Route::get('/Dashboard', 'HomeController@Dashboard')->name('home');


Route::group(['prefix' => 'task'], function () {

    Route::get('list', [
        'uses' => 'TaskController@getList',
        'as' => 'task.list'
    ]);

    Route::get('get/{id}', [
        'uses' => 'TaskController@getTask',
        'as' => 'task.get'
    ]);

    Route::get('listJson',[
       'uses' => 'TaskController@getListJson',
       'as' => 'task.listJson'
    ]);

    Route::get('add', [
	    'uses' => 'TaskController@getAdd',
	    'as' => 'task.add'
	]);

    Route::post('add', [
        'uses' => 'TaskController@postAdd',
        'as' => 'task.add'
    ]);

    Route::get('update/{id}', [
        'uses' => 'TaskController@getEdit',
        'as' => 'task.edit'
    ]);

    Route::post('update', [
        'uses' => 'TaskController@postUpdate',
        'as' => 'task.update'
    ]);

    Route::get('delete/{id}', [
        'uses' => 'TaskController@getDelete',
        'as' => 'task.delete'
    ]);
});
