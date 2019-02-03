@extends('layouts.app')

@section('content')

  <section id="PageHeader">
    <div class="container">
  	<header class="bg-primary text-white">
  		<div class="container text-center">
  			<h1>Welcome to OverControl</h1>
  			<p class="lead">A simple tool to keep in trakt your tasks</p>
  		</div>
  	</header>
  </div>
  </section><!--Header-->
  
  <section id="AddNewTask">
  	<div class="container">
  		<div class="card">
  			<div class="card card-body">
  				<div class="card-title text-center">
  					<h5>Add new task</h5>
  				</div>
  				<div class="row">
  					<div class="col-xl-12">
  						<form>
  							<div class="form-group">
  								<div class="row">
  									<div class="col-xl-3">
  										<label for="exampleInputEmail1">Name</label>
  										<input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                          placeholder="Enter email">
  										</div>
  										<div class="col-xl-3">
  											<label for="exampleInputEmail1">Priority</label>
  											<input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                          placeholder="Enter email">
  											</div>
  											<div class="col-xl-3">
  												<label for="exampleInputEmail1">Start date</label>
  												<input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                          placeholder="Enter email">
  												</div>
  												<div class="col-xl-3">
  													<label class="hidden" for="">test</label>
  													<button class="form-control btn btn-primary" type="submit">Add it</button>
  												</div>
  											</div>
  										</div>
  									</form>
  								</div>
  							</div>
  						</div>
  					</div>
  				</div>
  			</section><!--Task Form-->
  			
  <section id="Chart1">
  	<div class="container">
  		<div class="card">
  			<div class="card-body">
  				<div class="row">
  					<div class="col-md-12">
  						<canvas id="myChart" width="400" height="100"></canvas>
  					</div>
  				</div>
  			</div>
  		</div>
  	</div>
  </section><!--Big chart-->
  
  <section id="ItemList">
  	<div class="container">
  		<div class="card">
  			<div class="card-body">
  				<div class="card-title">
  					<h5>Tasks</h5>
  				</div>
  				<div class="row">
  					<div class="col-xl-12 mx-auto">
  						<table class="table">
  							<thead>
  								<tr>
  									<th scope="col">ID</th>
  									<th scope="col">Name</th>
  									<th scope="col">State</th>
  									<th scope="col">Difficulty</th>
  									<th scope="col">Priority</th>
  									<th scope="col">Start</th>
  									<th scope="col">Time postponed</th>
  									<th scope="col">End date</th>
  									<th scope="col">Duration time</th>
  								</tr>
  							</thead>
  							<tbody>
  								<tr>
  									<th scope="row">1</th>
  									<td>Mark</td>
  									<td>Otto</td>
  									<td>@mdo</td>
  								</tr>
  								<tr>
  									<th scope="row">2</th>
  									<td>Jacob</td>
  									<td>Thornton</td>
  									<td>@fat</td>
  								</tr>
  								<tr>
  									<th scope="row">3</th>
  									<td>Larry</td>
  									<td>the Bird</td>
  									<td>@twitter</td>
  								</tr>
  							</tbody>
  						</table>
  					</div>
  				</div>
  			</div>
  		</div>
  	</div>
  </section><!--Task table-->
  
  <section id="Chart2">
  	<div class="container">
  		<div class="card">
  			<div class="card-body">
  				<div class="row">
  					<div class="col-md-6">
  						<canvas id="myChart2" width="100" height="50"></canvas>
  					</div>
  					<div class="col-md-6">
  						<canvas id="myChart3" width="100" height="50"></canvas>
  					</div>
  				</div>
  			</div>
  		</div>
  	</div>
  </section><!--Button Charts-->

@endsection

