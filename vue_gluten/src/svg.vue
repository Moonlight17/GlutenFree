<template>
  <span>
    <svg id="NoneLike" v-if="name=='svg-NoneLike'" version="1.1" x="0px" y="0px" viewBox="0 0 51.997 51.997">
      <g>
        <g>
              <path id="NoneLikeBody"  d="M23.99294,15.87192l1.01585-0.88887c1.39679-1.22748,3.11808-1.83417,4.85349-1.83417    c2.03169,0,4.03517,0.83243,5.48839,2.45496c2.59605,2.93467,2.41263,7.35077-0.33862,10.0597l-9.82842,8.73568    c-0.67944,0.60256-1.70193,0.60256-2.38137,0l-9.81431-8.73568c-2.75125-2.69481-2.93467-7.12503-0.33862-10.0597    c1.45322-1.62253,3.4567-2.45496,5.48839-2.45496c1.7213,0,3.4567,0.60669,4.85349,1.83417L23.99294,15.87192" />
              <path id="NoneLikeBorder" d="M23.99294,15.87192l1.01585-0.88887c1.39679-1.22748,3.11808-1.83417,4.85349-1.83417c2.03169,0,4.03517,0.83243,5.48839,2.45496    c2.59605,2.93467,2.41263,7.35077-0.33862,10.0597l-9.82842,8.73568c-0.67944,0.60256-1.70193,0.60256-2.38137,0l-9.81431-8.73568    c-2.75125-2.69481-2.93467-7.12503-0.33862-10.0597c1.45322-1.62253,3.4567-2.45496,5.48839-2.45496    c1.7213,0,3.4567,0.60669,4.85349,1.83417L23.99294,15.87192" />
              <path id="NoneLikeTop" d="M13.97946,19.68624c0.10696-0.4492,0.2748-0.88792,0.50438-1.30326c0.18132-0.32803,0.40115-0.64148,0.6599-0.93398    c1.0309-1.15101,2.45214-1.74152,3.8934-1.74152" />
              <path id="NoneLikeBottom" d="M14.55714,23.5316c-0.29234-0.49406-0.49641-1.02862-0.61064-1.57971" />
        </g>
      </g>
    </svg>
    <svg id="ExistsLike" v-if="name=='svg-ExistsLike'" version="1.1" x="0px" y="0px" viewBox="0 0 51.997 51.997">
        <g>
            <g>
                <path id="ExistsLikeBorder"  d="M23.99294,15.87192l1.01585-0.88887c1.39679-1.22748,3.11808-1.83417,4.85349-1.83417    c2.03169,0,4.03517,0.83243,5.48839,2.45496c2.59605,2.93467,2.41263,7.35077-0.33862,10.0597l-9.82842,8.73568    c-0.67944,0.60256-1.70193,0.60256-2.38137,0l-9.81431-8.73568c-2.75125-2.69481-2.93467-7.12503-0.33862-10.0597    c1.45322-1.62253,3.4567-2.45496,5.48839-2.45496c1.7213,0,3.4567,0.60669,4.85349,1.83417L23.99294,15.87192" />
                <path id="ExistsLikeBody" d="M23.99294,15.87192l1.01585-0.88887c1.39679-1.22748,3.11808-1.83417,4.85349-1.83417c2.03169,0,4.03517,0.83243,5.48839,2.45496    c2.59605,2.93467,2.41263,7.35077-0.33862,10.0597l-9.82842,8.73568c-0.67944,0.60256-1.70193,0.60256-2.38137,0l-9.81431-8.73568    c-2.75125-2.69481-2.93467-7.12503-0.33862-10.0597c1.45322-1.62253,3.4567-2.45496,5.48839-2.45496    c1.7213,0,3.4567,0.60669,4.85349,1.83417L23.99294,15.87192" />
                <path id="ExistsLikeTop" d="M13.97946,19.68624c0.10696-0.4492,0.2748-0.88792,0.50438-1.30326c0.18132-0.32803,0.40115-0.64148,0.6599-0.93398    c1.0309-1.15101,2.45214-1.74152,3.8934-1.74152" />
                <path id="ExistsLikeBottom" d="M14.55714,23.5316c-0.29234-0.49406-0.49641-1.02862-0.61064-1.57971" />
            </g>
        </g>
    </svg>
  </span>
</template>
<style>
#NoneLike{
    margin-left: 84%;
    width: 50px;
    height: 50px;
}
#NoneLikeBorder{
    fill:none;
    stroke:rgb(255, 115, 0);
    stroke-width:0.7;
    stroke-linecap:round;
    stroke-linejoin:round;
    stroke-miterlimit:10;
}
#NoneLikeBody{
    fill:white
}
#NoneLikeTop{
    fill:none;
    stroke:rgb(255, 115, 0);
    stroke-width:0.7;
    stroke-linecap:round;
    stroke-linejoin:round;
    stroke-miterlimit:10;
}
#NoneLikeBottom{
    fill:none;
    stroke: rgb(255, 115, 0);
    stroke-width:0.7;
    stroke-linecap:round;
    stroke-linejoin:round;
    stroke-miterlimit:10;
}







#ExistsLike{
    margin-left: 84%;
    width: 50px;
    height: 50px;
}
#ExistsLikeBorder{
    fill:none;
    stroke:rgb(255, 0, 0);
    stroke-width:0.7;
    stroke-linecap:round;
    stroke-linejoin:round;
    stroke-miterlimit:10;
}
#ExistsLikeBody{
    fill:red
}
#ExistsLikeTop{
    fill:none;
    stroke:white;
    stroke-width:0.7;
    stroke-linecap:round;
    stroke-linejoin:round;
    stroke-miterlimit:10;
}
#ExistsLikeBottom{
    fill:none;
    stroke: white;
    stroke-width:0.7;
    stroke-linecap:round;
    stroke-linejoin:round;
    stroke-miterlimit:10;
}

</style>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true
    }
  }
};
</script>