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

    public function getStartDateAttribute($value){
        $MaskedValue = date("Y-m-d",strtotime($value));
        if($MaskedValue == "1970-01-01"){
            return "";
        }
        return $MaskedValue;
    }

    public function getEndDateAttribute($value){
        $MaskedValue = date("Y-m-d",strtotime($value));
        if($MaskedValue == "1970-01-01"){
            return "";
        }
        return $MaskedValue;
    }
}
