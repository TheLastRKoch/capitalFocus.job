<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Task;

class TaskController extends Controller
{
    public function getTask($id){
    	
    }
    
    public function getList(){
    	
    }
    
    public function getCreate(){
    	return view('task.create');
    }
    
    public function postCreate(Request $request){
    	$task = new Task([
    		''	
		])
    }
    
    public function getUpdate($id){
    	
    }
    
    public function getDelete(){
    	
    }
}
