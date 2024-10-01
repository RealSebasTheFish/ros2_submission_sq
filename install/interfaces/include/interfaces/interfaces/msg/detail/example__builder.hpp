// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Example.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__EXAMPLE__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__EXAMPLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/example__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Example_name
{
public:
  Init_Example_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::msg::Example name(::interfaces::msg::Example::_name_type arg)
  {
    msg_.name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Example msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Example>()
{
  return interfaces::msg::builder::Init_Example_name();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__EXAMPLE__BUILDER_HPP_
