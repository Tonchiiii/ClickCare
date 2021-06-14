$(document).ready(function()
{   
    $('#pain_scale1').hide();
    $('#submitNo1').hide();
    $('#submitYes1').hide();
                            
    $('#followupYes1').change(function()
    {
        if($('#followupYes1').is(':checked'))
        {
            $('#pain_scale1').fadeIn('slow');
            $('#submitNo1').fadeOut('slow');
                                        
        }
        else if($('#followupNo1').is(':checked'))
        {
        $('#pain_scale1').fadeOut('slow');
                                        
        }
        else{
            $('#pain_scale1').fadeOut('slow');
                                        
        }
    });
                            
        $('#followupNo1').change(function()
        {
            if($('#followupNo1').is(':checked'))
            {
                $('#pain_scale1').fadeOut('slow');
                $('#submitNo1').fadeIn('slow');
                }
                            
        });
                            
        $('#followup_mild1').change(function()
        {
            if($('#followup_mild1').is(':checked'))
            {
                $('#submitYes1').fadeIn('slow');
            }
        });
                            
                                $('#followup_moderate1').change(function()
                                {
                                    if($('#followup_moderate1').is(':checked'))
                                    {
                                        $('#submitYes1').fadeIn('slow');
                                    }
                                });
                            
                                $('#followup_severe1').change(function()
                                {
                                    if($('#followup_severe1').is(':checked'))
                                    {
                                        $('#submitYes1').fadeIn('slow');
                                    }
                                });
                            
                                $('#followup_worst1').change(function()
                                {
                                    if($('#followup_worst1').is(':checked'))
                                    {
                                        $('#submitYes1').fadeIn('slow');
                                    }
                                });
                            
                                
                            
                            });