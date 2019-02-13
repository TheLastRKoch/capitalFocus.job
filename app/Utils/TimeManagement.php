<?php
/**
 * Created by PhpStorm.
 * User: TheLastRkoch
 * Date: 12/02/2019
 * Time: 9:12 PM
 */

namespace App\Utils;

use Carbon\Carbon;

class TimeManagement
{
    /**
     * Calculate the relative time between the two times
     * @param $StartDate Start date of the task
     * @param $EndDate End date of the task
     * @return relative time
     */
    public function CalcPeriodTime($StartDate, $EndDate){
        return $EndDate->diffForHumans($StartDate);

    }

    /**
     * Calculate the postponed time
     * @param $StartDate
     * @return mixed
     */
    public function CalcTimePostponed($StartDate){
        return Carbon::now()->diffForHumans($StartDate);
    }
}
