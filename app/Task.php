<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Task extends Model
{
    protected $fillable = [
        'Name',
        'State',
        'Difficulty',
        'Priority',
        'StartDate',
        'TimePostponed',
        'EndDate',
        'PeriodTime'
    ];
}
