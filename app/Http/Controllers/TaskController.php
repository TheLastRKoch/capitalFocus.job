<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Task;
use Repositories\TaskRepository;

class TaskController extends Controller
{
    public function getTask($id){
    	
    }
    
    public function getList(){
    	$Tasks = Task::all();
    	return view('task.list', ['Tasks'=>$Tasks]);
    }

    public function getListJson(){
        $Tasks = Task::all();
        return $Tasks->toJson();
    }
    
    public function getAdd(){
    	return view('task.add');
    }
    
    public function postAdd(Request $request){
        $task = new Task([
            'Name' => $request->input('Name'),
            'State' => $request->input('State'),
            'Difficulty' => $request->input('Difficulty'),
            'Priority' => $request->input('Priority'),
            'StartDate' => $request->input('StartDate'),
            'TimePostponed' => $request->input('TimePostponed'),
            'EndDate' => $request->input('EndDate'),
            'PeriodTime' => $request->input('PeriodTime')
        ]);
        $task->save();
    }
    
    public function getUpdate($id){
    	
    }
    
    public function getDelete(){
    	
    }
}
