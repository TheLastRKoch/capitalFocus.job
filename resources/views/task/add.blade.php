@extends('layouts.app')

@section('content')

<section id='Page Header'>
    <div class="container">
        <div class="row pt-4">
          <div class="offset-1 col-xl-10 offset-1 text-xl-center">
            <h2>Add a task</h2>
            <p class="lead">Add a new task to remeber later ;).</p>
          </div>
        </div>
      </div>
</section>

<section id='Form'>
	<div class="container">
		<div class="row">

           <div class="offset-1 col-xl-10 offset-1">
               <div class="card">
                   <div class="card-body">
                       <form action="{{route('task.add')}}" method="post">
                           <div class="form-group">
                               <label for="title">Name</label>
                               <input type="text" class="form-control" id="txtName" name="Name" value="{{$Task->Name}}">
                           </div>
                           <div class="form-group">
                               <label for="content">State</label>
                               <input type="text" class="form-control" id="content" name="State" value="{{$Task->State}}">
                           </div>
                           <div class="form-group">
                               <label for="content">Difficulty</label>
                               <input type="text" class="form-control" id="txtDifficulty" name="Difficulty" value="{{$Task->Difficulty}}">
                           </div>
                           <div class="form-group">
                               <label for="content">Priority</label>
                               <input type="text" class="form-control" id="txtPriority" name="Priority" value="{{$Task->Priority}}">
                           </div>
                           <div class="form-group">
                               <label for="content">Start Date</label>
                               <input type="text" class="form-control" id="txtStartDate" name="StartDate" value="{{$Task->StartDate}}">
                           </div>
                           <div class="form-group">
                               <label for="content">Time Postponed</label>
                               <input type="text" class="form-control" id="txtTimePostponed" name="TimePostponed" value="{{$Task->TimePostponed}}">
                           </div>
                           <div class="form-group">
                               <label for="content">End Date</label>
                               <input type="text" class="form-control" id="txtEndDate" name="EndDate" value="{{$Task->EndDate}}">
                           </div>
                           <div class="form-group">
                               <label for="content">Period Time</label>
                               <input type="text" class="form-control" id="txtPeriodTime" name="PeriodTime" value="{{$Task->PeriodTime}}">
                           </div>
                           {{csrf_field()}}
                           <button type="submit" class="btn btn-primary btn-lg btn-block">Submit</button>
                       </form>
                   </div>
               </div>
           </div>

	    </div>
    </div>
</section>

@endsection
