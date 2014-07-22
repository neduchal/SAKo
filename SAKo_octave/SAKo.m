function sakoFunc = SAKo
  sakoFunc.submit = @submit;
  sakoFunc.serialize = @serialize;
end

function str = serialize(result)
  str = "";
  for i = 1 : size(result, 2);
      str = [str, '.' result(i).param_name, '#'];
      for j = 1 : size(result(i).param_value,1)
        for k = 1 : size(result(i).param_value,2)      
          str = [str, num2str(result(i).param_value(j,k)), ','];
        end
          str = str(1:end-1);      
          str = [str, ';'];
      end
      str = str(1:end-1);
  end
  str = str(2:end);
end


function submit(login, passwd, taskStr, result)

resultStr = serialize(result);
URL = 'http://neduchal.cz/zdo/SAKo/index.php';
str = urlread(URL, 'post', {'login', login, 'passwd', passwd, 'taskStr', taskStr, 'result', resultStr});

display(str)

end
