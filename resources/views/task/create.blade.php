@extends('layouts.app')

@section('content')

<section id='Page Header'>
    <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto">
            <h2>Add a task</h2>
            <p class="lead">Add a new task to remeber later ;).</p>
          </div>
        </div>
      </div>
</section>

<section id='Form'>
	<div class="container">
		<div class="row">
        <div class="col-md-8 offset-md-2">
            <form action="{{route('task.create')}}" method="post">
                <div class="form-group">
                    <label for="title">Name</label>
                    <input type="text" class="form-control" id="txtName" name="Name">
                </div>  
                <div class="form-group">
                    <label for="content">State</label>
                    <input type="text" class="form-control" id="content" name="State">
                </div>
                <div class="form-group">
                    <label for="content">Difficulty</label>
                    <input type="text" class="form-control" id="txtDifficulty" name="Difficulty">
                </div>
                <div class="form-group">
                    <label for="content">Priority</label>
                    <input type="text" class="form-control" id="txtPriority" name="Priority">
                </div>
                <div class="form-group">
                    <label for="content">Start Date</label>
                    <input type="text" class="form-control" id="txtStartDate" name="StartDate">
                </div>
                <div class="form-group">
                    <label for="content">Time Postponed</label>
                    <input type="text" class="form-control" id="txtTimePostponed" name="TimePostponed">
                </div>
                <div class="form-group">
                    <label for="content">End Date</label>
                    <input type="text" class="form-control" id="txtEndDate" name="EndDate">
                </div>
                <div class="form-group">
                    <label for="content">Period Time</label>
                    <input type="text" class="form-control" id="txtPeriodTime" name="PeriodTime">
                </div>
                {{csrf_field()}}
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
	</div>
</section>

@endsection