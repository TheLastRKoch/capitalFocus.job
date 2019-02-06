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
    	$Task = new Task([]);
        return view('task.add', ['Task'=>$Task]);
    }
    
    public function postAdd(Request $request){
        $Task = new Task([
            'Name' => $request->input('Name'),
            'State' => $request->input('State'),
            'Difficulty' => $request->input('Difficulty'),
            'Priority' => $request->input('Priority'),
            'StartDate' => $request->input('StartDate'),
            'TimePostponed' => $request->input('TimePostponed'),
            'EndDate' => $request->input('EndDate'),
            'PeriodTime' => $request->input('PeriodTime')
        ]);
        $Task->save();
        return redirect()->route('task.list');
    }
    
    public function getUpdate($id){
        $Task = Task::find($id);
        return view('task.add', ['Task'=>$Task]);
    }

    public function postUpdate(Request $request){
        $OldTask = Task::find($request->input('id'));
        $OldTask->Name =$request->input('Name');
        $OldTask->State =$request->input('State');
        $OldTask->Difficulty =$request->input('Difficulty');
        $OldTask->Priority =$request->input('Priority');
        $OldTask->StartDate =$request->input('StartDate');
        $OldTask->TimePostponed =$request->input('TimePostponed');
        $OldTask->EndDate =$request->input('EndDate');
        $OldTask->PeriodTime =$request->input('PeriodTime');
        $OldTask->save();
        return redirect()->route('task.list');
    }
    
    public function getDelete($id){
        $Task = Task::find($id);
        $Task->delete();
        return redirect()->route('task.list');
    }
}
