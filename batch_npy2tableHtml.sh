#!/bin/zsh

# source other config 
# source config_1.sh
source "$1"
# source ??/my_env/bin/activate
# WORKDIR=
# EXEC_MODES=("train")
# DATABASE_NAMES=("db_name")
# START_STEP=0
# END_STEP=10  # 任意の終了ステップを指定
# START_IDX_MEMORY=1
# END_IDX_MEMORY=1  # 任意の終了メモリインデックスを指定
# IDC_DEVICE=("0" "1")

# for 2d array
for exec_mode in ${EXEC_MODES[@]}  # 任意の実行モードを指定
do
  for database_name in ${DATABASE_NAMES[@]}  # 任意のデータベース名を指定
  do
    for step in {${START_STEP}..${END_STEP}}
    do
      for idx_memory in {${START_IDX_MEMORY}..${END_IDX_MEMORY}}
      do
        for idx_device in ${IDC_DEVICE[@]}
        do
          table_name="mode-${exec_mode}_dbname-${database_name}_step-${step}_memoryIndex-${idx_memory}_deviceIdx-${idx_device}"
          python main.py npy2tablehtml "$WORKDIR" "$exec_mode" "$database_name" "$step" "$idx_memory" "$idx_device" "$table_name" > ${WORKDIR}/${table_name}.html
        done
      done
    done
  done
done


# for 3d array
for exec_mode in ${EXEC_MODES[@]}  # 任意の実行モードを指定
do
  for i in {1..${#DATABASE_NAMES_3DARRAY[@]}}  # 任意のデータベース名を指定
  do
    # echo ${i}
    database_name=${DATABASE_NAMES_3DARRAY[${i}]}
    # echo ${database_name}
    for step in {${START_STEP}..${END_STEP}}
    do
      for idx_memory in {${START_IDX_MEMORY}..${END_IDX_MEMORY}}
      do
        for idx_device in ${IDC_DEVICE[@]}
        do
          for idx_3dim in {$EXPORT_RANGE_START_FOR_3D_DATABASE[${i}]..$EXPORT_RANGE_END_FOR_3D_DATABASE[${i}]}
          do
            table_name="mode-${exec_mode}_dbname-${database_name}_idx3dim-${idx_3dim}_step-${step}_memoryIndex-${idx_memory}_deviceIdx-${idx_device}"
            python main.py npy2tablehtml "$WORKDIR" "$exec_mode" "$database_name" "$step" "$idx_memory" "$idx_device" "$table_name" --dim3_idx "$idx_3dim" > ${WORKDIR}/${table_name}.html
          done
        done
      done
    done
  done
done

