#include "sysinc.h"
#include "module.h"

static int item_timeout = 0;
static ZBX_METRIC keys[] =
{
  {NULL}
};

int zbx_module_api_version(void)
{
  return ZBX_MODULE_API_VERSION;
}

void zbx_module_item_timeout(int timeout)
{
  item_timeout = timeout;
}

int zbx_module_init(void)
{
  srand(time(NULL));
  return ZBX_MODULE_OK;
}

int zbx_module_uninit(void)
{
  return ZBX_MODULE_OK;
}

static void example_history_log_cb(const ZBX_HISTORY_LOG *history, int history_num)
{
  int i;
  for (i = 0; i < history_num; i++)
  {
    FILE *file;
    file = fopen("./sample_log.txt", "a");
    fprintf(file, "itemid: %d, value: %s ¥n", history[i].itemid, history[i].value);
    fclose(file);
  }
}

static void example_history_float_cb(const ZBX_HISTORY_FLOAT *history, int history_num)
{
  int i;
  for (i = 0; i < history_num; i++)
  {
    /* do something with history[i].itemid, history[i].clock, history[i].ns, history[i].value,... */
  }
}

static void example_history_integer_cb(const ZBX_HISTORY_INTEGER *history, int history_num)
{
  int i;
  for (i = 0; i < history_num; i++)
  {
    /* do something with history[i].itemid, history[i].clock, history[i].ns, history[i].value,... */
  }
}

static void example_history_string_cb(const ZBX_HISTORY_STRING *history, int history_num)
{
  int i;
  for (i = 0; i < history_num; i++)
  {
    /* do something with history[i].itemid, history[i].clock, history[i].ns, history[i].value,... */
  }
}

static void example_history_text_cb(const ZBX_HISTORY_TEXT *history, int history_num)
{
  int i;
  for (i = 0; i < history_num; i++)
  {
    /* do something with history[i].itemid, history[i].clock, history[i].ns, history[i].value,... */
  }
}

ZBX_HISTORY_WRITE_CBS zbx_module_history_write_cbs(void)
{
  static ZBX_HISTORY_WRITE_CBS example_callbacks =
  {
    example_history_float_cb,
    example_history_integer_cb,
    example_history_string_cb,
    example_history_text_cb,
    example_history_log_cb
  };
  return example_callbacks;
}
